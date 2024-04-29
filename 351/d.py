h, w = list(map(int, input().split()))

s_s = []
for i in range(h):
    elem = list(input())
    s_s.append(elem)


def up(i, j):
    if i == 0:
        return i, j
    return i - 1, j


def down(i, j):
    if i == h - 1:
        return i, j
    return i + 1, j


def left(i, j):
    if j == 0:
        return i, j
    return i, j - 1


def right(i, j):
    if j == w - 1:
        return i, j
    return i, j + 1


def is_surround_sharp(i, j):
    current_posting = s_s[i][j]
    if current_posting == "#":
        raise ValueError("This is a wall.")
    if up(i, j) == "#":
        return True
    if down(i, j) == "#":
        return True
    if left(i, j) == "#":
        return True
    if right(i, j) == "#":
        return True
    return False


for i in range(h):
    for j in range(w):
        if s_s[i][j] == "#":
            continue
        while True:
            if is_surround_sharp(i, j):
                record_point = 1
                continue
            if s_s[i][j] == "#":
                continue
