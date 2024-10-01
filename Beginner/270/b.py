x, y, z = map(int, input().split())


def is_hammeer_need(x, y, z):
    if x > y > 0:
        return True
    if x < y < 0:
        return True
    return False


if is_hammeer_need(x, y, z):
    if x > 0:
        if z > y > 0:
            print(-1)
        else:
            if z > x:
                print(x)
            else:
                print(abs(z) + abs(z - x))
    else:
        if 0 > y > z:
            print(-1)
        else:
            if z < x:
                print(abs(x))
            else:
                print(abs(z) + abs(z - x))
else:
    print(abs(x))
