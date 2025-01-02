a, b, c, d = map(int, input().split())


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


for i in range(a, b + 1):
    prime_flag = False
    for j in range(c, d + 1):
        sum_num = i + j
        if is_prime(sum_num):
            prime_flag = True
            break
    if not prime_flag:
        print("Takahashi")
        exit()

print("Aoki")
