n, d = map(int, input().split())
xy_n = [tuple(map(int, input().split())) for _ in range(n)]


set_xy = set()
set_xy.add(xy_n[0])

is_infected = [False] * n


while set_xy:
    xy = set_xy.pop()
    for i in range(n):
        if is_infected[i]:
            continue
        if (xy[0] - xy_n[i][0]) ** 2 + (xy[1] - xy_n[i][1]) ** 2 <= d**2:
            set_xy.add(xy_n[i])
            is_infected[i] = True

for i in range(n):
    if is_infected[i]:
        print("Yes")
    else:
        print("No")
