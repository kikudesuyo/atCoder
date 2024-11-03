h, w, k = map(int, input().split())
s_hw = [list(input()) for _ in range(h)]
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]


VISITED = [[False] * w for _ in range(h)]


def dfs(row, col, dist):
    if dist == k:
        return 1
    count = 0
    for dr, dc in directions:
        current_row, current_col = row + dr, col + dc
        if (
            0 <= current_row < h
            and 0 <= current_col < w
            and not VISITED[current_row][current_col]
            and s_hw[current_row][current_col] == "."
        ):
            VISITED[current_row][current_col] = True
            count += dfs(current_row, current_col, dist + 1)
            VISITED[current_row][current_col] = False
    return count


sum_num = 0
for r in range(h):
    for c in range(w):
        if s_hw[r][c] == ".":
            VISITED[r][c] = True
            sum_num += dfs(r, c, 0)
            VISITED[r][c] = False
print(sum_num)
