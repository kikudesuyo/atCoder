from collections import deque

h, w = map(int, input().split())
c_hw = [list(input()) for _ in range(h)]

base_vectors = [(0, 1), (1, 0), (0, -1), (-1, 0)]


d = deque()
for i in range(h):
    for j in range(w):
        if c_hw[i][j] == ".":
            d.append(([(i, j)], (-100, -100)))

ans = -1
# 過去の全ての座標、前回の向きを持っておく
while d:
    coordinates, vector = d.popleft()
    (start_x, start_y) = coordinates[0]
    (current_x, current_y) = coordinates[-1]
    for dx, dy in base_vectors:
        # 逆方向はスキップ(条件1の3<=kと条件2の移動先が相異なること満たす)
        if (dx, dy) == (
            -vector[0],
            -vector[1],
        ):
            continue
        nx, ny = current_x + dx, current_y + dy
        if (nx, ny) == coordinates[0]:
            ans = max(ans, len(coordinates))
            continue
        if (
            0 <= nx < h
            and 0 <= ny < w
            and c_hw[nx][ny] == "."
            and (nx, ny) not in coordinates
        ):
            d.append((coordinates + [(nx, ny)], (dx, dy)))


print(ans)
