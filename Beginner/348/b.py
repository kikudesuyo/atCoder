n = int(input())

plots = {}
for i in range(n):
    plot = list(map(int, input().split()))
    plots[i] = plot

distances = []
for i in range(n):
    i_x, i_y = plots[i]
    max_distance_num = 0
    max_distance = 0
    for j in range(n):
        j_x, j_y = plots[j]
        distance = (i_x - j_x) ** 2 + (i_y - j_y) ** 2
        if distance > max_distance:
            max_distance_num = j + 1
            max_distance = distance
    print(max_distance_num)
