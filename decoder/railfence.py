import itertools


def encode_railfence(s: str, rail: int = 3):
    rows = ["" for i in range(rail)]
    T = rail * 2 - 2

    rows[0] = s[::T]
    for i in range(1, rail - 1):
        rows[i] = "".join([x[0] + x[1] for x in itertools.zip_longest(s[i::T], s[T - i::T], fillvalue='')])
    rows[rail - 1] = s[rail - 1::T]
    return "".join(rows)


def decode_railfence(s: str, rail: int = 3):
    T = rail * 2 - 2
    repeat = len(s) // T
    left = len(s) % T
    positions = ["" for i in range(T)]

    start = 0
    end = repeat + (1 if left > 0 else 0)
    positions[0] = s[start:end]

    for i in range(1, rail - 1):
        start = end
        end = end + repeat * 2 + (1 if left > i else 0) + (1 if left > T - i else 0)
        positions[i] = s[start:end:2]
        positions[T - i] = s[start + 1:end:2]

    positions[rail - 1] = s[end:]
    return "".join(["".join(x) for x in itertools.zip_longest(*positions, fillvalue='')])
