from collections import deque

q = int(input())

queries = [input() for _ in range(q)]

d = deque(tuple())

for r_query in queries:
    query = r_query.split()
    if query[0] == "1":
        d.append((int(query[1]), int(query[2])))
    elif query[0] == "2":
        left = int(query[1])
        cnt = 0
        while left > 0:
            x, c = d.popleft()
            if c > left:
                d.appendleft((x, c - left))
                cnt += left * x
                break
            left -= c
            cnt += c * x
        print(cnt)
