h, w = map(int, input().split())
a_hw = [list(map(int, input().split())) for _ in range(h)]

alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(h):
    for j in range(w):
        if a_hw[i][j] == 0:
            a_hw[i][j] = "."
        else:
            a_hw[i][j] = alphabets[a_hw[i][j] - 1]


for row in a_hw:
    print("".join(row))
