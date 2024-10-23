n, q = map(int, input().split())
q_s = [input().split() for _ in range(q)]

coordinates = []
for i in range(n):
    coordinates.append((i + 1, 0))

front = []
back = coordinates
for query in q_s:
    if len(back) == 0:
        back = front[::-1]
        front = []
    if query[0] == "1":
        c = query[1]
        if c == "R":
            if len(front) == 0:
                top = (back[0][0] + 1, back[0][1])
            else:
                top = (front[-1][0] + 1, front[-1][1])
            front.append(top)
            back.pop()
        elif c == "L":
            if len(front) == 0:
                top = (back[0][0] - 1, back[0][1])
            else:
                top = (front[-1][0] - 1, front[-1][1])
            front.append(top)
            back.pop()
        elif c == "U":
            if len(front) == 0:
                top = (back[0][0], back[0][1] + 1)
            else:
                top = (front[-1][0], front[-1][1] + 1)
            front.append(top)
            back.pop()
        elif c == "D":
            if len(front) == 0:
                top = (back[0][0], back[0][1] - 1)
            else:
                top = (front[-1][0], front[-1][1] - 1)
            front.append(top)
            back.pop()
    else:
        p = int(query[1])
        if p <= len(front):
            print(*front[-p])
        else:
            print(*back[p - len(front) - 1])
