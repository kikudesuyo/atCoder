import bisect

n = int(input())
x_n = list(map(int, input().split()))
p_n = list(map(int, input().split()))
q = int(input())

cumulative_sum = []
temp_sum = 0
for i in range(n):
    cumulative_sum.append(temp_sum + p_n[i])
    temp_sum += p_n[i]
ab_n = []
for i in range(q):
    ab = map(int, input().split())
    ab_n.append(ab)
for i in range(q):
    a, b = ab_n[i]
    left_idx = bisect.bisect_left(x_n, a)
    right_idx = bisect.bisect_right(x_n, b)
    if left_idx == right_idx:
        ans = 0
    else:
        if left_idx == 0:
            ans = cumulative_sum[right_idx - 1]
        else:
            ans = cumulative_sum[right_idx - 1] - cumulative_sum[left_idx - 1]
    print(ans)
