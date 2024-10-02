from itertools import combinations

n, w = map(int, input().split())
a_n = list(map(int, input().split()))


combi_3 = combinations(a_n, 3)
combi_2 = combinations(a_n, 2)
count = 0
arrays = []
for c in combi_3:
    if sum(c) <= w:
        arrays.append(sum(c))
for c in combi_2:
    if sum(c) <= w:
        arrays.append(sum(c))
for a in a_n:
    if a <= w:
        arrays.append(a)


print(len(set(arrays)))
