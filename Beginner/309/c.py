n, k = map(int, input().split())
ab_n = [list(map(int, input().split())) for _ in range(n)]

sorted_ab_n = sorted(ab_n, key=lambda x: x[0])
num = sum([b for a, b in sorted_ab_n])

if num <= k:
    print(1)
    exit()

for a, b in sorted_ab_n:
    num -= b
    if num <= k:
        print(a + 1)
        exit()

print(a + 1)
