l, r = input().split()

l_digit = len(l)
r_digit = len(r)

modulo = 10**9 + 7


def sum_d(a, l, n):
    return n * (a + l) // 2


total = 0
if l_digit == r_digit:
    total = sum_d(int(l), int(r), int(r) - int(l) + 1) * l_digit
    total %= modulo
    print(total)
    exit()

total += sum_d(int(l), 10**l_digit - 1, 10**l_digit - int(l)) * l_digit
total %= modulo
total += sum_d(10 ** (r_digit - 1), int(r), int(r) - 10 ** (r_digit - 1) + 1) * r_digit
total %= modulo

for i in range(l_digit + 1, r_digit):
    a = 10 ** (i - 1)
    l = 10**i - 1
    n = 9 * 10 ** (i - 1)
    total += sum_d(a, l, n) * i
    total %= modulo

print(total)
