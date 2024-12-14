from collections import deque

n, s = map(int, input().split())
a_n = list(map(int, input().split()))


t = a_n.copy()

arr = t + t[:-1]
r = s % sum(a_n)
cur = deque()
sum_num = 0

i = 0
while i < len(arr):
    while sum_num > r:
        sum_num -= cur.popleft()
    if sum_num == r:
        print("Yes")
        exit()
    cur.append(arr[i])
    sum_num += arr[i]
    i += 1

print("No")
