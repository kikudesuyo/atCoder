from bisect import bisect_left, bisect_right

n = int(input())
a_n = list(map(int, input().split()))

sorted_a = sorted(a_n)
cumulative_sum = [0] * (n + 1)
for i in range(n):
    cumulative_sum[i + 1] = cumulative_sum[i] + sorted_a[i]

total = sum(a_n)
ans = []
for i in range(n):
    idx = bisect_right(sorted_a, a_n[i])
    ans.append(total - cumulative_sum[idx])
print(*ans)
