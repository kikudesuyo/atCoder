a, b = map(int, input().split())


division = a // b
reminder = a % b
if reminder == 0:
    print(division)
else:
    print(division + 1)
