l1, r1, l2, r2 = map(int, input().split())


if r1 <= r2:
    if r1 <= l2:
        print(0)
    elif l1 <= l2 <= r1:
        print(r1 - l2)
    else:
        print(r1 - l1)
else:
    if r2 <= l1:
        print(0)
    elif l2 <= l1 <= r2:
        print(r2 - l1)
    elif l1 <= l2:
        print(r2 - l2)
