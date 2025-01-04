import re

n, q = map(int, input().split())
events = [input() for _ in range(q)]

is_callings = [False for _ in range(n)]
is_goings = [False for _ in range(n)]
num = 0
i = 0
for event in events:
    q = event.split()
    if q[0] == "1":
        num += 1
        is_callings[num - 1] = True
    elif q[0] == "2":
        person_num = int(q[1])
        is_goings[person_num - 1] = True
        is_callings[person_num - 1] = False
    elif q[0] == "3":
        while not is_callings[i]:
            i += 1
        print(i + 1)
