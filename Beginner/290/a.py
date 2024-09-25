n, m = map(int, input().split())
a_n = list(map(int, input().split()))
b_n = list(map(int, input().split()))

count = 0
for i in range(m):
    count += a_n[b_n[i] - 1]
print(count)
