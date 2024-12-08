h, w, d = map(int, input().split())
s_hw = [list(input()) for _ in range(h)]


def manhattan_arr(x, y, distance):
    manhattan_arr = []
    for row in range(h):
        for col in range(w):
            if abs(row - x) + abs(col - y) <= distance:
                manhattan_arr.append((row, col))
    return manhattan_arr


dict = {}
for r in range(h):
    for c in range(w):
        if s_hw[r][c] == "#":
            continue
        t_arr = [(r, c)]
        m_arr = manhattan_arr(r, c, d)
        for x, y in m_arr:
            if s_hw[x][y] == ".":
                t_arr.append((x, y))
        dict[(r, c)] = t_arr


max_ans = 0
for xy_1, arr_1 in dict.items():
    for xy_2, arr_2 in dict.items():
        if xy_1 == xy_2:
            continue
        extend = arr_1 + arr_2
        max_ans = max(max_ans, len(set(extend)))

print(max_ans)
