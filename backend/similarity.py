import os
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from highlight import find_copied_lines
from preprocess import preprocess_code, get_code_stats
from ast_similarity import extract_ast_tokens, compute_ast_similarity
from fingerprint import fingerprint_similarity, compute_fingerprint

# ---------------------------------------------------------------------
# CONFIG
# ---------------------------------------------------------------------

MIN_LINES = 5
MIN_CHARS = 50
SIMILARITY_THRESHOLD = 20
TOP_N_RESULTS = 5

DATASET_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dataset")

# ---------------------------------------------------------------------
# ALGORITHM SIGNATURE DETECTION
# ---------------------------------------------------------------------

ALGORITHM_SIGNATURES = {
    "bubble_sort": {
        "patterns": [
            r"for.*for",
            r"swap|temp",
            r"\[.*\+\s*1\]",
        ],
        "keywords": {"swap", "temp", "bubble"},
        "min_matches": 1,
    },
    "merge_sort": {
        "patterns": [
            r"merge",
            r"mid|middle|half",
        ],
        "keywords": {"merge", "split", "mid"},
        "min_matches": 1,
    },
    "quick_sort": {
        "patterns": [
            r"pivot",
            r"partition",
        ],
        "keywords": {"pivot", "partition", "quick"},
        "min_matches": 1,
    },
}


def detect_algorithm(code_raw):

    code = code_raw.lower()
    scores = {}

    for algo, sig in ALGORITHM_SIGNATURES.items():

        score = 0

        for p in sig["patterns"]:
            if re.search(p, code):
                score += 2

        words = set(re.findall(r"[a-zA-Z_]+", code))
        score += len(words & sig["keywords"])

        if score >= sig["min_matches"]:
            scores[algo] = score

    ranked = sorted(scores.items(), key=lambda x: -x[1])

    return ranked


def get_algorithm_family(filename):

    base = os.path.splitext(filename)[0]
    base = re.sub(r"_\d+$", "", base)
    base = re.sub(r"_(py|c|cpp|java)$", "", base)

    return base


# ---------------------------------------------------------------------
# DATASET CACHE
# ---------------------------------------------------------------------

class DatasetCache:

    def __init__(self):

        self.files = []
        self.processed = {}
        self.ast_tokens = {}
        self.fingerprints = {}
        self.raw = {}
        self.loaded = False

    def load(self):

        self.files.clear()
        self.processed.clear()
        self.ast_tokens.clear()
        self.fingerprints.clear()
        self.raw.clear()

        if not os.path.isdir(DATASET_DIR):
            self.loaded = True
            return

        for filename in os.listdir(DATASET_DIR):

            if not filename.endswith((".py", ".c", ".cpp", ".java")):
                continue

            path = os.path.join(DATASET_DIR, filename)

            try:

                with open(path, "r", encoding="utf-8", errors="ignore") as f:
                    raw = f.read()

                self.files.append(filename)
                self.raw[filename] = raw

                self.processed[filename] = preprocess_code(raw)

                # fingerprint caching
                self.fingerprints[filename] = compute_fingerprint(raw)

                if filename.endswith(".py"):
                    self.ast_tokens[filename] = extract_ast_tokens(raw)

            except:
                continue

        self.loaded = True

    def get_files_by_family(self, family):

        return [f for f in self.files if get_algorithm_family(f) == family]


_cache = DatasetCache()


def get_cache():

    if not _cache.loaded:
        _cache.load()

    return _cache


# ---------------------------------------------------------------------
# SIMILARITY ENGINE
# ---------------------------------------------------------------------

def compare_code(uploaded_file):

    cache = get_cache()

    with open(uploaded_file, "r", encoding="utf-8", errors="ignore") as f:
        uploaded_raw = f.read()

    lines, chars = get_code_stats(uploaded_raw)

    if lines < MIN_LINES or chars < MIN_CHARS:

        return {
            "error": "File too small for plagiarism analysis",
            "details": f"{lines} lines / {chars} chars",
            "algorithm_detected": "Unknown",
            "similarity": {},
            "copied_lines": {},
            "score_details": {},
        }

    uploaded_processed = preprocess_code(uploaded_raw)

    is_python = uploaded_file.endswith(".py")
    uploaded_ast_tokens = extract_ast_tokens(uploaded_raw) if is_python else None

    # compute fingerprint once
    uploaded_fp = compute_fingerprint(uploaded_raw)

    # ------------------------------------------------
    # algorithm detection
    # ------------------------------------------------

    detected = detect_algorithm(uploaded_raw)
    primary_family = detected[0][0] if detected else None

    if primary_family:
        compare_files = cache.get_files_by_family(primary_family)
    else:
        compare_files = list(cache.files)

    if not compare_files:

        return {
            "similarity": {},
            "copied_lines": {},
            "score_details": {},
            "algorithm_detected": primary_family or "Unknown",
        }

    # ------------------------------------------------
    # TF-IDF
    # ------------------------------------------------

    documents = [uploaded_processed]
    filenames = []

    for fname in compare_files:

        if fname in cache.processed:
            documents.append(cache.processed[fname])
            filenames.append(fname)

    vectorizer = TfidfVectorizer(
        analyzer="char_wb",
        ngram_range=(3, 5)
    )

    tfidf = vectorizer.fit_transform(documents)

    uploaded_vector = tfidf[0:1]

    results = {}
    copied = {}
    score_details = {}

    for i, fname in enumerate(filenames):

        dataset_vector = tfidf[i + 1:i + 2]

        similarity = cosine_similarity(uploaded_vector, dataset_vector)[0][0]

        length_factor = min(len(uploaded_processed), len(cache.processed[fname])) / \
                        max(len(uploaded_processed), len(cache.processed[fname]))

        tfidf_percentage = round(similarity * length_factor * 100, 2)

        # cached fingerprint comparison
        winnowing_score = fingerprint_similarity(
            uploaded_raw,
            cache.processed.get(fname, ""),
            fp1=uploaded_fp,
            fp2=cache.fingerprints.get(fname, set())
        )

        winnowing_percentage = round(winnowing_score * 100, 2)

        if is_python and fname.endswith(".py"):

            ast_sim = compute_ast_similarity(
                uploaded_ast_tokens,
                cache.ast_tokens.get(fname, [])
            )

            ast_percentage = round(ast_sim * length_factor * 100, 2)

            final_percent = (
                0.2 * tfidf_percentage
                + 0.3 * ast_percentage
                + 0.5 * winnowing_percentage
            )

        else:

            ast_percentage = 0.0

            final_percent = (
                0.4 * tfidf_percentage
                + 0.6 * winnowing_percentage
            )

        percent = round(final_percent, 2)

        if percent < SIMILARITY_THRESHOLD:
            continue

        results[fname] = percent

        score_details[fname] = {
            "tfidf_score": tfidf_percentage,
            "ast_score": ast_percentage,
            "winnowing_score": winnowing_percentage,
            "final_score": percent,
        }

        dataset_raw = cache.raw.get(fname, "")

        matched_lines = find_copied_lines(uploaded_raw, dataset_raw)

        if matched_lines:
            copied[fname] = matched_lines

    sorted_results = dict(
        sorted(results.items(), key=lambda x: -x[1])[:TOP_N_RESULTS]
    )

    copied_filtered = {k: copied[k] for k in sorted_results if k in copied}
    details_filtered = {k: score_details[k] for k in sorted_results if k in score_details}

    return {
        "similarity": sorted_results,
        "copied_lines": copied_filtered,
        "score_details": details_filtered,
        "algorithm_detected": primary_family or "Unknown",
        "total_files_compared": len(filenames),
    }