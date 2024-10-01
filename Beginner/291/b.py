n = int(input())
x_n = list(map(int, input().split()))

ascend_xn = sorted(x_n)

middle = ascend_xn[n : 4 * n]
print(sum(middle) / len(middle))
