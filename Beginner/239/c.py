x1, y1, x2, y2 = map(int, input().split())


# 距離ルート5の格子点
def get_grid_points(x, y):
    return [
        (x - 1, y - 2),
        (x - 1, y + 2),
        (x + 1, y - 2),
        (x + 1, y + 2),
        (x - 2, y - 1),
        (x - 2, y + 1),
        (x + 2, y - 1),
        (x + 2, y + 1),
    ]


first_grid_points = get_grid_points(x1, y1)
second_grid_points = get_grid_points(x2, y2)

for first_grid_point in first_grid_points:
    if first_grid_point in second_grid_points:
        print("Yes")
        exit()
print("No")
