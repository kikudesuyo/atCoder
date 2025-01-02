from bisect import bisect_left

n, m = map(int, input().split())

xyc_m = [input().split() for _ in range(m)]

blacks = []
whites = []
for x, y, c in xyc_m:
    x, y = int(x), int(y)
    if c == "B":
        blacks.append((x, y))
    else:
        whites.append((x, y))

if len(blacks) == 0:
    print("Yes")
    exit()
elif len(whites) == 0:
    print("Yes")
    exit()


def preprocess_b(b_list):
    b_list.sort(key=lambda b: (b[0], b[1]))
    processed = []
    max_y = -1
    for bx, by in reversed(b_list):
        if by > max_y:
            processed.append((bx, by))
            max_y = by
    return list(reversed(processed))


procesed_blacks = preprocess_b(blacks)
for w_x, w_y in sorted(whites):
    idx = bisect_left(procesed_blacks, (w_x, w_y))
    if idx == len(procesed_blacks):
        continue
    if procesed_blacks[idx][1] >= w_y:
        print("No")
        exit()
print("Yes")
