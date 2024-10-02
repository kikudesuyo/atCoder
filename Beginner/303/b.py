from itertools import combinations

n, m = map(int, input().split())
a_mn = [list(map(int, input().split())) for _ in range(m)]


combi = list(combinations(range(1, n + 1), 2))

for i in range(m):
    a_n = a_mn[i]
    for j in range(n - 1):
        if (a_n[j], a_n[j + 1]) in combi:
            combi.remove((a_n[j], a_n[j + 1]))
        if (a_n[j + 1], a_n[j]) in combi:
            combi.remove((a_n[j + 1], a_n[j]))

print(len(combi))
