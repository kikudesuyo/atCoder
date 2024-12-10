n, q = map(int, input().split())
s = list(input())
q_s = [list(map(int, input().split())) for _ in range(q)]

i = 0
for query in q_s:
    t, x = query
    if t == 1:
        i += x
        i %= n
    if t == 2:
        print(s[x - 1 - i])
