from collections import defaultdict

n = int(input())
a_n = list(map(int, input().split()))

d = defaultdict(int)


arr = []
for idx in range(n):
    if a_n[idx] in d:
        arr.append(d[a_n[idx]])
    else:
        arr.append(-1)
    d[a_n[idx]] = idx + 1

print(*arr)
