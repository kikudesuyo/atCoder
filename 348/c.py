n = int(input())

dict = {}
color_history = []
for i in range(n):
    bean = list(map(int, input().split()))
    yummy_num, color = bean
    if color in color_history:
        same_color_beans = dict[color]
        same_color_beans.append(bean)
        dict[color] = same_color_beans
    else:
        dict[color] = [bean]
        color_history.append(color)

yummy_mins = {}
for key, value in dict.items():
    yummy_min = 10000000000000000000
    for i in value:
        if i[0] < yummy_min:
            yummy_min = i[0]
    yummy_mins[key] = yummy_min

# print(yummy_mins)


max = 0
for key, value in yummy_mins.items():
    if value > max:
        max = value

print(max)
