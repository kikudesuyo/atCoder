from collections import deque

n = int(input())
a_n = list(map(int, input().split()))
c = sum(a_n) // 10
a_n = a_n + a_n

t = 0
d = deque()
for e in a_n:
    d.append(e)
    t += e
    if t == c and len(d) <= n:
        print("Yes")
        exit()
    while t > c:
        p = d.popleft()
        t -= p

print("No")
