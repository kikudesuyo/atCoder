h, w = map(int, input().split())
a_hw = [list(map(int, input().split())) for _ in range(h)]
b_hw = [list(map(int, input().split())) for _ in range(h)]

c, r = 0, 0
cnt = 0
while c < w - 1 and r < h - 1:
    a, b = a_hw[r][c], b_hw[r][c]
    diff = b - a
    a_hw[r][c] += diff
    a_hw[r][c + 1] += diff
    a_hw[r + 1][c] += diff
    a_hw[r + 1][c + 1] += diff
    cnt += abs(diff)
    if c == w - 2:
        r += 1
        c = 0
    else:
        c += 1

if a_hw == b_hw:
    print("Yes")
    print(cnt)
else:
    print("No")
