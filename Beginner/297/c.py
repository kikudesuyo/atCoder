h, w = map(int, input().split())
s_h = [list(input()) for _ in range(h)]


for i in range(h):
    for j in range(w - 1):
        if s_h[i][j : j + 2] == ["T", "T"]:
            s_h[i][j : j + 2] = ["P", "C"]

for i in range(h):
    print("".join(s_h[i]))
