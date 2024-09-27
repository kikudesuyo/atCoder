r, c = map(int, input().split())

a_11, a_12 = map(int, input().split())
a_21, a_22 = map(int, input().split())

if r == 1:
    if c == 1:
        print(a_11)
    else:
        print(a_12)
else:
    if c == 1:
        print(a_21)
    else:
        print(a_22)
