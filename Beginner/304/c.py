n, d = map(int, input().split())
xy_n = [tuple(map(int, input().split())) for _ in range(n)]


is_infected = [False] * n
is_infected[0] = True

set_xy = set()
set_xy.add(xy_n[0])

while set_xy:
    x, y = set_xy.pop()
    for i in range(n):
        if is_infected[i]:
            continue
        if (x - xy_n[i][0]) ** 2 + (y - xy_n[i][1]) ** 2 <= d**2:
            set_xy.add(xy_n[i])
            is_infected[i] = True

for i in range(n):
    if is_infected[i]:
        print("Yes")
    else:
        print("No")
