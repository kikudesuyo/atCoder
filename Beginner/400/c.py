import math

n = int(input())


good_nums = []


def add_good_num(target, i):
    val = 2
    while val <= target:
        if math.isqrt(val) ** 2 == val:
            good_nums.append(val * (2**i))
        val *= 2


n //= 2
i = 1
cnt = 0
while n >= 1:
    max_square = math.isqrt(n)
    if max_square == 0:
        break
    print("n", n)
    cnt += max_square
    add_good_num(n, i)
    n //= 2
    i += 1

print(cnt)
print("good_nums", good_nums)
print(len(good_nums))
