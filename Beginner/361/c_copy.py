n, k = map(int, input().split())
a_s = list(map(int, input().split()))
a_s.sort()


# 最小値とするためには橋をどんどん取り除いて行けば良い。
ans = float("inf")
for i in range(k + 1):
    ans = min(ans, a_s[i + n - k - 1] - a_s[i])
print(ans)
