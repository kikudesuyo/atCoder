h = int(input())

day = 0
length = 1
while True:
    if h < length:
        print(day + 1)
        break
    day += 1
    length = length + 2**day
