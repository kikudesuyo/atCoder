a, b, c = map(int, input().split())


if b > c:
    c = c + 24
    if b < a + 24 < c:
        print("No")
    else:
        print("Yes")
else:
    if b < a < c:
        print("No")
    else:
        print("Yes")
