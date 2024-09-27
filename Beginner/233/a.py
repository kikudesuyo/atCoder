x, y = map(int, input().split())

num = y - x

if num <= 0:
    print(0)
    exit()
reminder = num % 10
if reminder == 0:
    print(num // 10)

else:
    print(num // 10 + 1)
