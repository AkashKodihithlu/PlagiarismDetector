import os, re
import sys
sys.path.append('a:/plagiarism/backend')
from similarity import get_algorithm_family

# Test get_algorithm_family
tests = {
    'bubble_sort_1.py': 'bubble_sort',
    'bubble_sort_py_5.py': 'bubble_sort',
    'bubble_sort_cpp_3.cpp': 'bubble_sort',
    'dfs_c_11.c': 'dfs',
    'quick_sort_java_2.java': 'quick_sort',
    'lcs_3.py': 'lcs',
}
for f, expected in tests.items():
    result = get_algorithm_family(f)
    assert result == expected, f"{f}: got {result!r}, expected {expected!r}"
print("All get_algorithm_family tests passed")

# Count dataset files
dataset_dir = 'a:/plagiarism/backend/dataset'
files = [f for f in os.listdir(dataset_dir) if f.endswith(('.py','.c','.cpp','.java'))]
print(f"Total dataset files: {len(files)}")
assert len(files) >= 490, f"Expected ~500 files, got {len(files)}"

# Verify families
families = set(get_algorithm_family(f) for f in files)
expected_families = {'bubble_sort','quick_sort','merge_sort','binary_search','dfs','bfs','dijkstra','knapsack','fibonacci','lcs'}
assert families == expected_families, f"Missing: {expected_families - families}, Extra: {families - expected_families}"
print(f"All 10 algorithm families present: {sorted(families)}")

# Check file sizes
for f in files:
    path = os.path.join(dataset_dir, f)
    # only check generated files which have _lang_ format
    if re.search(r'_(py|c|cpp|java)_\d+\.', f):
        lines = open(path, encoding='utf-8', errors='ignore').read().splitlines()
        assert len(lines) >= 20, f"{f} has only {len(lines)} lines"

print("All files have sufficient length")
