n, x = map(int, input().split())
ab_n = [list(map(int, input().split())) for _ in range(n)]


dp = [[False for _ in range(x + 1)] for _ in range(n + 1)]
dp[0][0] = True

for i in range(n):
    a, b = ab_n[i]
    for j in range(x):
        if dp[i][j]:
            if j + a <= x:
                dp[i + 1][j + a] = True
            if j + b <= x:
                dp[i + 1][j + b] = True

if dp[n][x]:
    print("Yes")
else:
    print("No")
