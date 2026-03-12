def generate_fibonacci_sequence(length):
    """Generate fibonacci sequence of given length"""
    if length <= 0:
        return []
    if length == 1:
        return [0]

    seq = [0, 1]
    for _ in range(2, length):
        next_val = seq[-1] + seq[-2]
        seq.append(next_val)
    return seq


if __name__ == "__main__":
    fib_seq = generate_fibonacci_sequence(10)
    print("Sequence:", fib_seq)
