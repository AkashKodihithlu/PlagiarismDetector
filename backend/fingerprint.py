"""
Winnowing fingerprint algorithm for source-code plagiarism detection.
Uses k-gram hashing + sliding-window minimum selection + Jaccard similarity.
"""

import re

# ── tunables ────────────────────────────────────────────────────────
K = 25          # k-gram size  (larger ⇒ fewer false positives)
WINDOW = 4      # winnowing window size

# ── source-code normalisation ──────────────────────────────────────

def _normalise(code: str) -> str:
    """Strip comments, literals, and whitespace so renaming / reformatting
    does not affect fingerprints."""
    # block comments  /* ... */
    code = re.sub(r"/\*[\s\S]*?\*/", "", code)
    # Python docstrings
    code = re.sub(r'"""[\s\S]*?"""', "", code)
    code = re.sub(r"'''[\s\S]*?'''", "", code)
    # single-line comments
    code = re.sub(r"//.*", "", code)
    code = re.sub(r"#.*", "", code)
    # string literals
    code = re.sub(r'"[^"]*"', '""', code)
    code = re.sub(r"'[^']*'", "''", code)
    # collapse all whitespace
    code = re.sub(r"\s+", "", code)
    return code.lower()

# ── winnowing core ─────────────────────────────────────────────────

def _kgrams(text: str, k: int):
    """Yield hashed k-grams."""
    for i in range(len(text) - k + 1):
        yield hash(text[i:i + k])


def _winnow(text: str, k: int = K, w: int = WINDOW) -> set:
    """Return the set of selected fingerprint hashes."""
    hashes = list(_kgrams(text, k))
    if not hashes:
        return set()

    fingerprints = set()
    prev_min_idx = -1

    for i in range(len(hashes) - w + 1):
        window = hashes[i:i + w]
        # right-most minimum (tie-break toward the right)
        min_val = min(window)
        min_idx = i + w - 1 - window[::-1].index(min_val)
        if min_idx != prev_min_idx:
            fingerprints.add(min_val)
            prev_min_idx = min_idx

    return fingerprints

# ── public API ─────────────────────────────────────────────────────

def compute_fingerprint(text: str) -> set:
    """Normalise source code and return its winnowed fingerprint set.
    This is the cacheable unit — call once per file and store the result."""
    return _winnow(_normalise(text))


def fingerprint_similarity(text1: str, text2: str,
                           fp1: set = None, fp2: set = None) -> float:
    """Jaccard similarity of Winnowing fingerprints.  Returns 0.0 – 1.0.

    If pre-computed fingerprint sets *fp1* / *fp2* are supplied they are
    used directly, avoiding redundant normalisation + hashing.
    """
    if fp1 is None:
        fp1 = compute_fingerprint(text1)
    if fp2 is None:
        fp2 = compute_fingerprint(text2)

    if not fp1 and not fp2:
        return 0.0
    intersection = fp1 & fp2
    union = fp1 | fp2
    return len(intersection) / len(union) if union else 0.0
