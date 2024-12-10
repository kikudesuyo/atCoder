n, m = map(int, input().split())
a_n = list(map(int, input().split()))

t = sum(a_n[:m])
sum_nums = [t]
for i in range(n - m):
    t = t - a_n[i] + a_n[i + m]
    sum_nums.append(t)

max_num = 0
for i in range(m):
    max_num += a_n[i] * (i + 1)

t = max_num
for i in range(1, n - m + 1):
    t = t - sum_nums[i - 1] + a_n[i + m - 1] * m
    max_num = max(t, max_num)
print(max_num)
