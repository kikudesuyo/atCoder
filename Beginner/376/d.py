from collections import deque

n, m = map(int, input().split())
ab_m = [list(map(int, input().split())) for _ in range(m)]
sorted_ab_m = sorted(ab_m, key=lambda x: x[0])

dict_ab = {}
for i in range(1, n + 1):
    dict_ab[i] = []
for ab in sorted_ab_m:
    a, b = ab
    dict_ab[a].append(b)


queue = deque([(1, 0)])
visited = set()
while queue:
    a, count = queue.popleft()
    if a == 1 and count > 0:
        print(count)
        exit()
    if a not in visited:
        visited.add(a)
        for ending_point in dict_ab[a]:
            starting_p = ending_point
            queue.append((starting_p, count + 1))
print(-1)
