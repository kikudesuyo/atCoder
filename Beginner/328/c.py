n, q = map(int, input().split())
s = input()
lr_q = [list(map(int, input().split())) for _ in range(q)]

consecutive_idxes = [0] * n
for i in range(n - 1):
    if s[i] == s[i + 1]:
        consecutive_idxes[i + 1] = 1

cumulative_sum = [0] * n
for i in range(1, n):
    cumulative_sum[i] = cumulative_sum[i - 1] + consecutive_idxes[i]


for lr in lr_q:
    l, r = lr
    print(cumulative_sum[r - 1] - cumulative_sum[l - 1])
