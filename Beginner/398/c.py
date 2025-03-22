from collections import defaultdict

n = int(input())
a_n = list(map(int, input().split()))

d = defaultdict(list)
for i in range(n):
    d[a_n[i]].append(i + 1)

max_num = 0
max_idx = -1
for key, val in d.items():
    if len(val) == 1:
        if max_num < key:
            max_num = key
            max_idx = val[0]

print(max_idx)
