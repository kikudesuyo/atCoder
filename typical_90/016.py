n = int(input())
a, b, c = map(int, input().split())

min_num = 10**4
for x in range(n // a + 1):
    for y in range(n // b + 1):
        ab_sum = a * x + b * y
        if x + y > 9999:
            break
        if ab_sum > n:
            break
        if (n - (ab_sum)) % c == 0:
            z = (n - (ab_sum)) // c
            min_num = min(min_num, x + y + z)

print(min_num)
