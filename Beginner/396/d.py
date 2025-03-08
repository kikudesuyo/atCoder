from collections import defaultdict, deque

n, m = map(int, input().split())
uvw = [list(map(int, input().split())) for _ in range(m)]

d = defaultdict(list)
for i in range(m):
    u, v, w = uvw[i]
    d[u].append((v, w))
    d[v].append((u, w))

routes = []
queue = deque([(1, [1], [])])

while queue:
    current, route, cost = queue.popleft()
    if current == n:
        routes.append((route, cost))
        continue

    for next, w in d[current]:
        if next not in route:
            queue.append((next, route + [next], cost + [w]))

ans = float("inf")
for route, costs in routes:
    xor_cost = 0
    for c in costs:
        xor_cost ^= c
    ans = min(ans, xor_cost)

print(ans)
