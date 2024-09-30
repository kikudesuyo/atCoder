n = int(input())
xy_n = [list(map(int, input().split())) for _ in range(n)]


max_num = 0
for i in range(len(xy_n)):
    for j in range(len(xy_n)):
        if i >= j:
            continue
        x1, y1 = xy_n[i]
        x2, y2 = xy_n[j]
        max_num = max(max_num, ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5)
print(max_num)
