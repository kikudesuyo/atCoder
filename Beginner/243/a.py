v, a, b, c = map(int, input().split())


count = 0
while True:
    if count % 3 == 0:
        v -= a
    if count % 3 == 1:
        v -= b
    if count % 3 == 2:
        v -= c
    count += 1
    if v < 0:
        if count % 3 == 0:
            print("T")
        if count % 3 == 1:
            print("F")
        if count % 3 == 2:
            print("M")
        break
