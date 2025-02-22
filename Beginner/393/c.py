from collections import defaultdict

n, m = map(int, input().split())
uv = [list(map(int, input().split())) for i in range(m)]

cnt = 0
d = defaultdict(set)
for i in range(m):
    s, l = min(uv[i]), max(uv[i])
    if s == l:
        cnt += 1
        continue
    length = len(d[s])
    d[s].add(l)
    if len(d[s]) == length:
        cnt += 1

print(cnt)
