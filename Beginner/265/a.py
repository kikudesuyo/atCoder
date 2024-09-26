x, y, n = map(int, input().split())

is_superior_x = x * 3 < y

count = 0
reminder = 0
if is_superior_x:
    count = n * x
else:
    if n % 3 == 0:
        count = n // 3 * y
    else:
        count = n // 3 * y
        reminder = n % 3
        if reminder == 1:
            count += x
        elif reminder == 2:
            count += 2 * x
print(count)
