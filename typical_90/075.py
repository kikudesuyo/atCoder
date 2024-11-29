import math

n = int(input())

arr = []
while n % 2 == 0:
    arr.append(2)
    n //= 2

f = 3
while f * f <= n:
    if n % f == 0:
        arr.append(f)
        n //= f
    else:
        f += 2
if n != 1:
    arr.append(n)
l = math.log2(len(arr))

if 2 ** int(l) == len(arr):
    print(int(l))
else:
    print(int(l) + 1)
