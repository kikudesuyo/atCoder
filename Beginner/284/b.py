t = int(input())


queries = []
for _ in range(t):
    queries.append([int(input()), list(map(int, input().split()))])

for query in queries:
    n, a_n = query
    count = 0
    for a in a_n:
        if a % 2 != 0:
            count += 1
    print(count)
