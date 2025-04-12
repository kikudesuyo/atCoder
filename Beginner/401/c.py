from collections import deque

n, k = map(int, input().split())

if n < k:
    print(1)
    exit()

d = deque()
for i in range(k):
    d.append(1)

cur_sum_num = k
for i in range(n - k):
    d.append(cur_sum_num)
    cur_sum_num += (cur_sum_num - d.popleft()) % 10**9


print(cur_sum_num % 10**9)
