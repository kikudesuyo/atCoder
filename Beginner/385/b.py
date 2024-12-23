h, w, x, y = map(int, input().split())
s_hw = [list(input()) for _ in range(h)]
t = list(input())


cur_row, cur_col = x - 1, y - 1
housees = set()
if s_hw[cur_row][cur_col] == "@":
    housees.add((cur_row, cur_col))

for d in t:
    if d == "L":
        if s_hw[cur_row][cur_col - 1] == "#" or cur_col == 0:
            continue
        cur_col -= 1
        if s_hw[cur_row][cur_col] == "@" and (cur_row, cur_col) not in housees:
            housees.add((cur_row, cur_col))
    elif d == "R":
        if s_hw[cur_row][cur_col + 1] == "#" or cur_col == w - 1:
            continue
        cur_col += 1
        if s_hw[cur_row][cur_col] == "@" and (cur_row, cur_col) not in housees:
            housees.add((cur_row, cur_col))
    elif d == "U":
        if s_hw[cur_row - 1][cur_col] == "#" or cur_row == 0:
            continue
        cur_row -= 1
        if s_hw[cur_row][cur_col] == "@" and (cur_row, cur_col) not in housees:
            housees.add((cur_row, cur_col))
    elif d == "D":
        if s_hw[cur_row + 1][cur_col] == "#" or cur_row == h - 1:
            continue
        cur_row += 1
        if s_hw[cur_row][cur_col] == "@" and (cur_row, cur_col) not in housees:
            housees.add((cur_row, cur_col))

print(cur_row + 1, cur_col + 1, len(housees))
