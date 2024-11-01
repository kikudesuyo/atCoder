n, x, y = map(int, input().split())


red_num = 1
blue_num = 0
for _ in range(n - 1):
    blue_num = blue_num + red_num * x
    red_num += blue_num
    blue_num = blue_num * y


print(blue_num)
