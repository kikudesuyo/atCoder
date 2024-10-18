h, w = map(int, input().split())
g_hw = [list(input()) for _ in range(h)]

x, y = [0, 0]

memo = [[False] * w for _ in range(h)]

while True:
    if memo[x][y]:
        print(-1)
        exit()
    memo[x][y] = True
    if g_hw[x][y] == "U":
        if x == 0:
            print(x + 1, y + 1)
            exit()
        x -= 1
    if g_hw[x][y] == "D":
        if x == h - 1:
            print(x + 1, y + 1)
            exit()
        x += 1
    if g_hw[x][y] == "L":
        if y == 0:
            print(x + 1, y + 1)
            exit()
        y -= 1
    if g_hw[x][y] == "R":
        if y == w - 1:
            print(x + 1, y + 1)
            exit()
        y += 1
