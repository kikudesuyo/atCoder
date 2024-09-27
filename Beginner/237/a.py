n = int(input())

if n < 0:
    if n >= -1 * 2**31:
        print("Yes")
        exit()
    else:
        print("No")
        exit()
else:
    if n < 2**31:
        print("Yes")
        exit()
    else:
        print("No")
        exit()
