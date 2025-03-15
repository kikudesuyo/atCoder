import math

n = int(input())

for A in range(1, 10**7):
    if (n - A**3) < 0:
        break
    if (n - A**3) % (3 * A) == 0:
        B = (n - A**3) // (3 * A)
        if math.isqrt(A**2 + 4 * B) ** 2 == A**2 + 4 * B:
            root_num = math.isqrt(A**2 + 4 * B)
            if (-A + root_num) % 2 == 0:
                y = (-A + root_num) // 2
                x = A + y
                if x != 0 and y != 0:
                    print(x, y)
                    exit()


print(-1)
