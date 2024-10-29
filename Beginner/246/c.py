n, k, x = map(int, input().split())
a_n = list(map(int, input().split()))


for i in range(n):
    q, r = a_n[i] // x, a_n[i] % x
    if q == 0:
        continue
    if k >= q:
        k -= q
        a_n[i] = r
    else:
        a_n[i] = (q - k) * x + r
        k = 0
        break

sorted_an = sorted(a_n, reverse=True)

if n <= k:
    print(0)
    exit()
for i in range(k):
    sorted_an[i] = 0

print(sum(sorted_an))
