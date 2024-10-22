from collections import deque

n, m = map(int, input().split())
uv_m = [list(map(int, input().split())) for _ in range(m)]

graph = {}
for i in range(n):
    graph[i] = []

for u, v in uv_m:
    graph[v - 1].append(u - 1)
    graph[u - 1].append(v - 1)


is_visited = [False] * n
cnt = 0
q = deque()
for i in range(n):
    if is_visited[i]:
        continue
    # BFSを実装
    cnt += 1
    is_visited[i] = True
    q.append(i)
    while q:
        c = q.popleft()
        for d in graph[c]:
            if is_visited[d]:
                continue
            is_visited[d] = True
            q.append(d)

print(cnt)
