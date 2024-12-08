import math

n = int(input())


def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


double_e_n = math.isqrt(n)


def get_not_eratos(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return [i for i in range(n + 1) if not is_prime[i]]


r_not_eratos = get_not_eratos(double_e_n)
not_eratos = [i for i in r_not_eratos if i > 2]


def prime_factorize(n):
    factors = []
    if n % 4 == 0 or n % 9 == 0:
        return []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    while n % 3 == 0:
        factors.append(3)
        n //= 3
    if len(factors) > 2:
        return []
    f = 5
    while f * f <= n:
        if len(factors) > 2:
            return []
        while n % f == 0:
            factors.append(f)
            n //= f
        while n % (f + 2) == 0:
            factors.append(f + 2)
            n //= f + 2
        f += 6
    if n > 1:
        factors.append(n)
    if len(factors) == 2:
        return factors
    return []


doubles = []
for elem in not_eratos:
    f = prime_factorize(elem)
    if len(set(f)) == 2 and len(f) == 2:
        doubles.append(elem)


e_n = int(n ** (1 / 8))
eight_cnt = 0
for i in range(1, e_n + 1):
    if is_prime(i):
        eight_cnt += 1

print(len(doubles) + eight_cnt)
