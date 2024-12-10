from collections import deque

n = int(input())
s_n = list(map(int, input().split()))
t_n = list(map(int, input().split()))


ans = t_n.copy()

dq = deque()
for i in range(n):
    dq.append((t_n[i], i))

while dq:
    t, i = dq.popleft()
    if ans[i] < t:
        continue
    ans[i] = t
    dq.append((t + s_n[i], (i + 1) % n))

for a in ans:
    print(a)
