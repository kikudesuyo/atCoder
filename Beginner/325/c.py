from collections import deque

h, w = map(int, input().split())
s_h = [list(input()) for _ in range(h)]


vectors = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, -1), (-1, 1)]

sensers = set()
for i in range(h):
    for j in range(w):
        if s_h[i][j] == "#":
            sensers.add((i, j))

d = deque()
cnt = 0
while sensers:
    d.append(sensers.pop())
    while d:
        x, y = d.popleft()
        for dx, dy in vectors:
            nx, ny = x + dx, y + dy
            if 0 <= nx < h and 0 <= ny < w and s_h[nx][ny] == "#":
                if (nx, ny) in sensers:
                    d.append((nx, ny))
                    sensers.discard((nx, ny))
    cnt += 1

print(cnt)
