a, b = map(int, input().split())

if a == 1:
    if b == 10:
        print("Yes")
        exit()

if b == 1:
    if a == 10:
        print("Yes")
        exit()
if abs(a - b) == 1:
    print("Yes")
else:
    print("No")
