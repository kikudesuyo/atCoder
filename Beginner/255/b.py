import math

n, k = map(int, input().split())
a_k = list(map(int, input().split()))
xy_n = [list(map(int, input().split())) for _ in range(n)]

light_arr = []
not_light_arr = xy_n.copy()
for elem in a_k:
    light_arr.append(xy_n[elem - 1])
    not_light_arr.remove(xy_n[elem - 1])

max_dis = 0

not_light_distances = [10**9] * len(not_light_arr)
for light_x, light_y in light_arr:
    for idx, not_xy in enumerate(not_light_arr):
        not_x, not_y = not_xy
        distance = math.sqrt((light_x - not_x) ** 2 + (light_y - not_y) ** 2)
        not_light_distances[idx] = min(not_light_distances[idx], distance)


print(max(not_light_distances))
