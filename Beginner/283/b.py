n = int(input())
a_n = list(map(int, input().split()))
q = int(input())
queries = [list(map(int, input().split())) for _ in range(q)]
for query in queries:
    if query[0] == 1:
        a_n[query[1] - 1] = query[2]
    elif query[0] == 2:
        print(a_n[query[1] - 1])
