n, m = map(int, input().split())
ab_n = [list(map(int, input().split())) for _ in range(m)]


dict = {}
losers = []
# 負け確実の人をリストに入れる
for a, b in ab_n:
    losers.append(b)
losers = list(set(losers))

if len(losers) == n - 1:
    for i in range(1, n + 1):
        if i not in losers:
            print(i)
else:
    print(-1)
