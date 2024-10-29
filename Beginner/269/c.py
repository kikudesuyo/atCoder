from itertools import product

n = int(input())
bin_n = bin(n)[2:]

arr = []
for b in bin_n:
    if b == "1":
        arr.append([0, 1])
    else:
        arr.append([0])

pro = list(product(*arr))
for e in pro:
    print(int("".join(map(str, e)), 2))
