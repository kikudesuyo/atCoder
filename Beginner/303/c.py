n, m, h, k = map(int, input().split())
s = input()
set_xy_m = set([tuple(map(int, input().split())) for _ in range(m)])

x, y = 0, 0
for q in s:
    if q == "R":
        x += 1
    elif q == "L":
        x -= 1
    elif q == "U":
        y += 1
    elif q == "D":
        y -= 1
    h -= 1
    if h == -1:
        print("No")
        exit()
    if (x, y) in set_xy_m:
        if h < k:
            h = k
            set_xy_m.discard((x, y))
print("Yes")
