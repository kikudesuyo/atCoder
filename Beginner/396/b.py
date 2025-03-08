from calendar import c
from collections import deque

q = int(input())
queries = [input() for _ in range(q)]

cards = deque()
for i in range(100):
    cards.append(0)

for r_q in queries:
    q = list(map(int, r_q.split()))
    if q[0] == 1:
        cards.appendleft(q[1])
    elif q[0] == 2:
        print(cards.popleft())
