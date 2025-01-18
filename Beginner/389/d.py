r = int(input())

j = 0
while 2 * j**2 + 2 * j + 1 < 2 * r**2:
    j += 1


def calc(i, j, r):
    return 2 * i**2 + 2 * i + 2 * j**2 + 2 * j + 1 - 2 * r**2


cnt = 0
for i in range(r):
    while calc(i, j, r) > 0:
        j -= 1
    cnt += j

print(cnt * 4 + 1)
