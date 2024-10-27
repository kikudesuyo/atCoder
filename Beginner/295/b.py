r, c = map(int, input().split())
b_rc = [list(input()) for _ in range(r)]

bomb_dict = {}
for i in range(r):
    for j in range(c):
        if not b_rc[i][j] in [".", "#"]:
            bomb_dict[(i, j)] = b_rc[i][j]


def manhattan_arr(x, y, n):
    arr = []
    for i in range(-n, n + 1):
        for j in range(-n, n + 1):
            if abs(i) + abs(j) <= n:
                arr.append((x + i, y + j))
    return arr


bomb_area = []
for (x, y), power in bomb_dict.items():
    arr = manhattan_arr(x, y, int(power))
    for x, y in arr:
        if 0 <= x < r and 0 <= y < c:
            bomb_area.append((x, y))

ans_arr = []

for i in range(r):
    ans = ""
    for j in range(c):
        if (i, j) in bomb_area:
            ans += "."
        else:
            if b_rc[i][j] == "#":
                ans += "#"
            else:
                ans += "."
    ans_arr.append(ans)

print("\n".join(ans_arr))
