from collections import defaultdict

n = int(input())
a_n = list(map(int, input().split()))
q = int(input())
queries = [input() for _ in range(q)]

add_num = 0

d = defaultdict(int)

for i in range(n):
    d[i] = a_n[i]

for query in queries:
    i_query = list(map(int, query.split()))
    if i_query[0] == 1:
        d = defaultdict(int)
        add_num = i_query[1]
    elif i_query[0] == 2:
        idx, num = i_query[1], i_query[2]
        d[idx - 1] += num
    elif i_query[0] == 3:
        idx = i_query[1]
        print(d[idx - 1] + add_num)
