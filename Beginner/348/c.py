n = int(input())

color_to_min_yummy = {}

for _ in range(n):
    yummy_num, color = map(int, input().split())
    if color in color_to_min_yummy.keys():
        if yummy_num < color_to_min_yummy[color]:
            color_to_min_yummy[color] = yummy_num
    else:
        color_to_min_yummy[color] = yummy_num

# 最大の美味しさを持つ豆の数を求める
if color_to_min_yummy:
    yummy_max = max(color_to_min_yummy.values())
    print(yummy_max)
