import itertools
import math

n, p, q = map(int, input().split())
a_n = list(map(int, input().split()))


conbinations = list(itertools.combinations(a_n, 5))

count = 0
for i in range(len(conbinations)):
    product = math.prod(conbinations[i])
    if product % p == q:
        count += 1
print(count)
