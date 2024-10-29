from collections import defaultdict
from itertools import combinations

n, k = map(int, input().split())
s_n = [list(input()) for _ in range(n)]

combis = []
for i in range(1, n + 1):
    t = list(combinations(range(n), i))
    combis.extend(t)

max_num = 0
for combi in combis:
    d = defaultdict(int)
    for idx in combi:
        string = s_n[idx]
        for s in string:
            d[s] += 1
    cnt = 0
    for value in d.values():
        if value == k:
            cnt += 1
    max_num = max(max_num, cnt)
print(max_num)
