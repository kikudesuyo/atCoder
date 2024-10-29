h, w = map(int, input().split())
s_hw = [list(input()) for _ in range(h)]


l, r = w - 1, 0
t, b = h - 1, 0


for i in range(h):
    for j in range(w):
        if s_hw[i][j] == "#":
            l = min(l, j)
            r = max(r, j)
            t = min(t, i)
            b = max(b, i)


for i in range(t, b + 1):
    for j in range(l, r + 1):
        if s_hw[i][j] == ".":
            print(i + 1, j + 1)
