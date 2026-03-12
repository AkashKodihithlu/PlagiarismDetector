import difflib

def find_copied_lines(code1, code2):

    # split lines and remove empty ones
    lines1 = [line.strip() for line in code1.split("\n") if line.strip()]
    lines2 = [line.strip() for line in code2.split("\n") if line.strip()]

    matcher = difflib.SequenceMatcher(None, lines1, lines2)

    copied = []

    for match in matcher.get_matching_blocks():
        for i in range(match.size):
            line = lines1[match.a + i]
            if line:  # ignore blank lines
                copied.append(line)

    return copied