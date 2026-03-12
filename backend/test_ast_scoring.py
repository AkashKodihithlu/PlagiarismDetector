import os
import sys
sys.path.append('a:/plagiarism/backend')
from similarity import compare_code, get_cache

def setup():
    os.makedirs('a:/plagiarism/uploads', exist_ok=True)
    # Preload cache so we don't count loading time
    print("Loading cache...")
    get_cache()
    
def test_upload(name, code, expected_algorithm=None):
    path = f'a:/plagiarism/uploads/{name}'
    with open(path, 'w', encoding='utf-8') as f:
        f.write(code)
        
    print(f"\\n--- Testing {name} ---")
    results = compare_code(path)
    
    print(f"Detected Algorithm: {results.get('algorithm_detected')}")
    print("Top matches:")
    sims = results.get('similarity', {})
    for k, v in sims.items():
        print(f"  {k}: {v}%")
        
    if expected_algorithm:
        # Check if the highest string match belongs to expected
        if sims:
            top_match = list(sims.keys())[0]
            assert expected_algorithm in top_match, f"Expected {expected_algorithm} to be top match, got {top_match}"
        else:
            print("WARNING: No matches found above threshold!")

if __name__ == '__main__':
    setup()
    
    # 1. Bubble Sort Variant
    bubble_code = """
def my_sort_function(items):
    # A completely different looking bubble sort
    length = len(items)
    for x in range(length):
        for y in range(0, length - x - 1):
            if items[y] > items[y + 1]:
                # Swap them
                t = items[y]
                items[y] = items[y+1]
                items[y+1] = t
    return items
    
# test it
data = [5, 2, 9, 1, 5, 6]
print(my_sort_function(data))
# extra padding to reach 20 lines
# padding
# padding
# padding
# padding
# padding
# padding
# padding
# padding
"""
    test_upload('test_bubble.py', bubble_code, 'bubble_sort')

    # 2. Quick Sort Variant
    quick_code = """
def quick_sort(array):
    if len(array) <= 1: 
        return array
    pivot = array[len(array) // 2]
    l = [x for x in array if x < pivot]
    m = [x for x in array if x == pivot]
    r = [x for x in array if x > pivot]
    return quick_sort(l) + m + quick_sort(r)

if __name__ == '__main__':
    print(quick_sort([5, 2, 9, 1, 5, 6]))

# extra padding
# padding
# padding
# padding
# padding
# padding
# padding
# padding
# padding
"""
    test_upload('test_quick.py', quick_code, 'quick_sort')
    
    # 3. Unrelated program
    unrelated_code = """
import os
import sys

def parse_logs(filepath):
    try:
        results = {}
        with open(filepath, 'r') as f:
            for n, line in enumerate(f):
                if 'ERROR' in line:
                    parts = line.split('-')
                    if len(parts) > 2:
                        error_type = parts[1].strip()
                        results[error_type] = results.get(error_type, 0) + 1
                        
        print(f"Parsed {n} lines.")
        for k, v in results.items():
            print(f"Error {k}: {v}")
    except FileNotFoundError:
        print("Log file missing.")
        
if __name__ == '__main__':
    parse_logs("/var/log/syslog")
"""
    test_upload('test_unrelated.py', unrelated_code)
    
    try:
        os.remove('a:/plagiarism/uploads/test_bubble.py')
        os.remove('a:/plagiarism/uploads/test_quick.py')
        os.remove('a:/plagiarism/uploads/test_unrelated.py')
    except:
        pass
