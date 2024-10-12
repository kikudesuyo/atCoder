import math

n = int(input())
xy_n = [list(map(int, input().split())) for _ in range(n)]

total = 0
current_xy = [0, 0]
for xy in xy_n:
    x, y = xy
    distance = math.sqrt((x - current_xy[0]) ** 2 + (y - current_xy[1]) ** 2)
    total += distance
    current_xy = xy
distance = math.sqrt((0 - current_xy[0]) ** 2 + (0 - current_xy[1]) ** 2)
total += distance
print(total)
