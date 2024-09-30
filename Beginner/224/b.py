h, w = map(int, input().split())

a_hw = [list(map(int, input().split())) for _ in range(h)]

for i in range(h - 1):
    for j in range(w - 1):
        a, b, c, d = a_hw[i][j], a_hw[i][j + 1], a_hw[i + 1][j], a_hw[i + 1][j + 1]
        if a + d > b + c:
            print("No")
            exit()
print("Yes")
