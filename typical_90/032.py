from itertools import permutations

n = int(input())
a_nn = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
xy = [list(map(int, input().split())) for _ in range(m)]


unfrendly_pairs = set((x - 1, y - 1) for x, y in xy)

p = list(permutations(range(n)))
c = []
for e in p:
    f = True
    for i in range(n - 1):
        if (e[i], e[i + 1]) in unfrendly_pairs or (e[i + 1], e[i]) in unfrendly_pairs:
            f = False
            break
    if f:
        c.append(e)


if len(c) == 0:
    print(-1)
    exit()

ans = 10**9
for e in c:
    s = 0
    for i in range(n):
        s += a_nn[e[i]][i]
    ans = min(ans, s)
print(ans)
