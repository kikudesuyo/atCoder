y = int(input())

reminder = y % 4

if reminder == 0:
    print(y + 2)
if reminder == 1:
    print(y + 1)
if reminder == 2:
    print(y)
if reminder == 3:
    print(y + 3)
