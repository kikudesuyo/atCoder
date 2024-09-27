h, w = map(int, input().split())
r, c = map(int, input().split())


left_idx, right_idx = r - 1, h - r
top_idx, bottom_idx = c - 1, w - c


if h == 1 and w == 1:
    print(0)
    exit()
if h == 1:
    if c == 1 or c == w:
        print(1)
        exit()
    else:
        print(2)
        exit()
if w == 1:
    if r == 1 or r == h:
        print(1)
        exit()
    else:
        print(2)
        exit()

if left_idx == 0 and bottom_idx == 0:
    print(2)
    exit()
if left_idx == 0 and top_idx == 0:
    print(2)
    exit()
if right_idx == 0 and bottom_idx == 0:
    print(2)
    exit()
if right_idx == 0 and top_idx == 0:
    print(2)
    exit()


if 0 in [left_idx, right_idx, top_idx, bottom_idx]:
    print(3)
    exit()
print(4)
