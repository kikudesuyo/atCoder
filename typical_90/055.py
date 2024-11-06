import itertools

n, p, q = map(int, input().split())
a_n = list(map(int, input().split()))


conbinations = itertools.combinations(a_n, 5)

count = 0
for a, b, c, d, e in conbinations:
    reminder = a % p * b % p * c % p * d % p * e % p
    if reminder == q:
        count += 1
print(count)
