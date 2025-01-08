n = int(input())


def calc_primes(max_limit):
    """エラトステネスの篩でmax_limit以下の素数を列挙"""
    is_prime = [True] * (max_limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(max_limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_limit + 1, i):
                is_prime[j] = False
    return [i for i in range(2, max_limit + 1) if is_prime[i]]


p_s = calc_primes(int(n ** (1 / 4)))
q_s = calc_primes(int(n ** (1 / 3)))

cnt = 0
for p in p_s:
    for q in q_s:
        if p < q and p * (q**3) <= n:
            cnt += 1
        if p * (q**3) > n:
            break


print(cnt)
