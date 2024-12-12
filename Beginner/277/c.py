from collections import deque, defaultdict
n = int(input())
ab_n = [list(map(int, input().split())) for _ in range(n)]

d = defaultdict(set)
for a,b in ab_n:
    d[a].add(b)
    d[b].add(a)
    
    
dq = deque()

visited = set()

dq.append(1)
ans = 1
while dq:
    v = dq.popleft()
    if v in visited:
        continue
    visited.add(v)
    ans = max(ans, v)
    for i in d[v]:
        if i not in visited:
            dq.append(i)

print(ans)