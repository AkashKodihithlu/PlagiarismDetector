import re

# Python keywords that indicate code STRUCTURE (keep these)
STRUCTURAL_KEYWORDS = {
    'def', 'class', 'if', 'elif', 'else', 'for', 'while', 'return',
    'try', 'except', 'finally', 'with', 'yield', 'lambda', 'import',
    'from', 'raise', 'break', 'continue', 'pass', 'and', 'or', 'not',
    'in', 'is', 'True', 'False', 'None', 'global', 'nonlocal',
    'async', 'await', 'assert', 'del',
}

# Common tokens to REMOVE (they appear in almost every program and cause false matches)
NOISE_TOKENS = {
    'print', 'input', 'main', 'int', 'str', 'float', 'bool',
    'void', 'char', 'double', 'long', 'short', 'unsigned', 'signed',
    'public', 'private', 'protected', 'static', 'const',
    'include', 'stdio', 'stdlib', 'iostream', 'using', 'namespace', 'std',
    'system', 'string', 'args', 'self', 'cls', 'super',
    '__init__', '__main__', '__name__',
}

# Algorithm-specific tokens that MATTER for distinguishing algorithms
ALGORITHM_TOKENS = {
    # sorting
    'swap', 'pivot', 'partition', 'merge', 'split', 'divide',
    'sorted', 'sort', 'bubble', 'quick', 'insertion', 'selection',
    'heapify', 'heap', 'sift',
    # searching
    'search', 'binary', 'linear', 'find', 'lookup', 'mid', 'middle',
    'low', 'high', 'left', 'right', 'target', 'key', 'found',
    # graph
    'graph', 'node', 'edge', 'vertex', 'neighbor', 'adjacent',
    'visited', 'queue', 'stack', 'bfs', 'dfs', 'dijkstra',
    'distance', 'weight', 'path', 'shortest', 'traverse',
    'popleft', 'heappush', 'heappop', 'priority',
    # dynamic programming
    'memo', 'cache', 'dp', 'table', 'knapsack', 'capacity',
    'fibonacci', 'fib', 'subsequence', 'lcs', 'optimal',
    'memoize', 'memoization', 'tabulation',
    # recursion
    'recursive', 'recurse', 'base', 'helper',
}


def preprocess_code(code):
    """
    Preprocess code for plagiarism detection.
    Preserves structural keywords and algorithm-specific tokens.
    Normalizes generic variable names.
    Removes noise tokens.
    """
    # remove single-line comments
    code = re.sub(r'#.*', '', code)
    code = re.sub(r'//.*', '', code)

    # remove multi-line comments and docstrings
    code = re.sub(r'/\*[\s\S]*?\*/', '', code)
    code = re.sub(r'"""[\s\S]*?"""', '', code)
    code = re.sub(r"'''[\s\S]*?'''", '', code)

    # remove string literals
    code = re.sub(r'"[^"]*"', '""', code)
    code = re.sub(r"'[^']*'", "''", code)

    # extract identifiers
    tokens = re.findall(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', code)

    processed_tokens = []
    for token in tokens:
        lower = token.lower()

        # skip noise tokens
        if lower in NOISE_TOKENS:
            continue

        # keep structural keywords as-is
        if token in STRUCTURAL_KEYWORDS:
            processed_tokens.append(token)
        # keep algorithm-specific tokens as-is
        elif lower in ALGORITHM_TOKENS:
            processed_tokens.append(lower)
        # normalize generic identifiers to VAR
        else:
            processed_tokens.append('VAR')

    return ' '.join(processed_tokens)


def get_code_stats(code):
    """Return line count and character count of non-empty code."""
    lines = [line.strip() for line in code.strip().split('\n') if line.strip()]
    return len(lines), len(code.strip())