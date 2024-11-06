n = int(input())
a_nn = [list(map(int, input().split())) for _ in range(n)]

product = 1
for elems in a_nn[1:]:
    product *= sum(elems)
    product %= 10**9 + 7
num = 0
a1 = a_nn[0]
for elem in a1:
    num += elem * product

print(num % (10**9 + 7))
