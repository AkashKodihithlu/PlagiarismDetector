import ast
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def extract_ast_tokens(code: str) -> list[str]:
    """
    Extract structural tokens from Python code.
    Returns a list of AST node type names.
    Ignores SyntaxErrors and returns an empty list.
    """
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return []
        
    tokens = [type(node).__name__ for node in ast.walk(tree)]
    return tokens

def compute_ast_similarity(tokens_a: list[str], tokens_b: list[str]) -> float:
    """
    Computes cosine similarity between two lists of AST tokens using TF-IDF.
    Returns a float between 0.0 and 1.0.
    """
    if not tokens_a or not tokens_b:
        return 0.0
        
    tokens_a_str = " ".join(tokens_a)
    tokens_b_str = " ".join(tokens_b)
    
    vectorizer = TfidfVectorizer(ngram_range=(1, 3))
    try:
        matrix = vectorizer.fit_transform([tokens_a_str, tokens_b_str])
        score = cosine_similarity(matrix[0:1], matrix[1:2])[0][0]
        return float(score)
    except ValueError:
        # e.g., empty vocabulary
        return 0.0
