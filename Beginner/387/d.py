from collections import deque

h, w = map(int, input().split())
s_h = [list(input()) for _ in range(h)]

row_vectors = [(1, 0), (-1, 0)]
col_vectors = [(0, 1), (0, -1)]

for i in range(h):
    for j in range(w):
        if s_h[i][j] == "S":
            start_idx = (i, j)
        if s_h[i][j] == "G":
            goal_idx = (i, j)

d = deque()
d.append((start_idx, 0, ""))

visited = [[[10**9] * w for _ in range(h)] for _ in range(2)]
while d:
    (r, c), cnt, direction = d.popleft()
    if direction in ["", "C"]:
        for vector in row_vectors:
            new_r = r + vector[0]
            new_c = c + vector[1]
            if 0 <= new_r < h and 0 <= new_c < w:
                if (
                    s_h[new_r][new_c] in [".", "G"]
                    and cnt + 1 < visited[0][new_r][new_c]
                ):
                    visited[0][new_r][new_c] = cnt + 1
                    d.append(((new_r, new_c), cnt + 1, "R"))
    if direction in ["R", ""]:
        for vector in col_vectors:
            new_r = r + vector[0]
            new_c = c + vector[1]
            if 0 <= new_r < h and 0 <= new_c < w:
                if (
                    s_h[new_r][new_c] in [".", "G"]
                    and cnt + 1 < visited[1][new_r][new_c]
                ):
                    visited[1][new_r][new_c] = cnt + 1
                    d.append(((new_r, new_c), cnt + 1, "C"))


if (
    visited[0][goal_idx[0]][goal_idx[1]] == 10**9
    and visited[1][goal_idx[0]][goal_idx[1]] == 10**9
):
    print(-1)
else:
    print(
        min(
            visited[0][goal_idx[0]][goal_idx[1]],
            visited[1][goal_idx[0]][goal_idx[1]],
        )
    )
