n = int(input())
s = input()

x, y = 0, 0


set_xy = set()
set_xy.add((x, y))
for i in s:
    if i == "L":
        x, y = x - 1, y
    elif i == "R":
        x, y = x + 1, y
    elif i == "U":
        x, y = x, y + 1
    elif i == "D":
        x, y = x, y - 1
    if (x, y) in set_xy:
        print("Yes")
        exit()
    else:
        set_xy.add((x, y))
print("No")
