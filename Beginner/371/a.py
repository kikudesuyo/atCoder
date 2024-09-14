x, y, z = input().split()

if x == ">":
    if y == ">":
        if z == ">":
            print("B")
        else:
            print("C")
    else:
        if z == ">":
            print("B")
        else:
            print("A")
else:
    if y == ">":
        if z == ">":
            print("A")
        else:
            print("B")
    else:
        if z == ">":
            print("C")
        else:
            print("B")
