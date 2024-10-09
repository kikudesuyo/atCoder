n, m, t = map(int, input().split())
a_n = list(map(int, input().split()))
xy_m = [list(map(int, input().split())) for _ in range(m)]

if m == 0:
    if t <= sum(a_n):
        print("No")
    else:
        print("Yes")
    exit()

current_time = t
bounus_idx = 0
for i in range(len(a_n)):
    if xy_m[bounus_idx][0] - 1 == i:
        current_time += xy_m[bounus_idx][1]
        if len(xy_m) - 1 > bounus_idx:
            bounus_idx += 1
    current_time -= a_n[i]
    if current_time <= 0:
        print("No")
        exit()
print("Yes")
