def compute_lcs(seq_a, seq_b):
    """Compute LCS length using bottom-up table"""
    rows = len(seq_a)
    cols = len(seq_b)

    table = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]

    row = 1
    while row <= rows:
        col = 1
        while col <= cols:
            if seq_a[row - 1] == seq_b[col - 1]:
                table[row][col] = table[row - 1][col - 1] + 1
            else:
                table[row][col] = max(table[row - 1][col], table[row][col - 1])
            col += 1
        row += 1

    return table[rows][cols]


if __name__ == "__main__":
    a = "ABCBDAB"
    b = "BDCAB"
    answer = compute_lcs(a, b)
    print(f"LCS of '{a}' and '{b}' is {answer}")
