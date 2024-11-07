from collections import defaultdict

n, q = map(int, input().split())
tab_q = [list(map(int, input().split())) for _ in range(q)]


users = defaultdict(set)

for query in tab_q:
    t, a, b = query
    if t == 1:
        users[a].add(b)
        pass
    elif t == 2:
        users[a].discard(b)
        pass
    elif t == 3:
        if b in users[a] and a in users[b]:
            print("Yes")
        else:
            print("No")
