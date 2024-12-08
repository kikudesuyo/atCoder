from collections import deque

h, w, d = map(int, input().split())
s_hw = [list(input()) for _ in range(h)]


dq = deque()
for r in range(h):
    for c in range(w):
        if s_hw[r][c] != "H":
            continue
        dq.append((r, c, 0))

vectors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
visited = [[False] * w for _ in range(h)]

cnt = len(dq)
while dq:
    x, y, distance = dq.popleft()  # 左側の要素を取り出す
    if distance == d:
        continue
    for v_x, v_y in vectors:
        if 0 <= x + v_x < h and 0 <= y + v_y < w and s_hw[x + v_x][y + v_y] == ".":
            if visited[x + v_x][y + v_y]:
                continue
            visited[x + v_x][y + v_y] = True
            dq.append((x + v_x, y + v_y, distance + 1))

dot_cnt = 0
for r in range(h):
    for c in range(w):
        if visited[r][c]:
            dot_cnt += 1
print(dot_cnt + cnt)
