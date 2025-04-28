from collections import deque

q = int(input())
queries = [input() for _ in range(q)]

d = deque()

for r in queries:
    q = r.split()
    if len(q) == 1:
        print(d.popleft())
    elif len(q) == 2:
        x = int(q[1])
        d.append(x)
