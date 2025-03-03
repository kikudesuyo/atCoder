from collections import defaultdict

n = int(input())
a_n = list(map(int, input().split()))

if len(set(a_n)) == n:
    print("-1")
    exit()

d = defaultdict(list)
for i in range(n):
    d[a_n[i]].append(i)

min_diff = float("inf")
for k, v in d.items():
    if len(v) < 2:
        continue
    min_d = float("inf")
    current_v = v[0]
    for elem in range(1, len(v)):
        min_d = min(min_d, v[elem] - current_v + 1)
        current_v = v[elem]
    min_diff = min(min_diff, min_d)

print(min_diff)
