from itertools import combinations

n, m = map(int, input().split())

arr = [i + 1 for i in range(m)]
c_s = list(combinations(arr, n))

for c in c_s:
    print(*c)
