n, k = map(int, input().split())
a_n = list(map(int, input().split()))
b_n = list(map(int, input().split()))

list = []

for i in range(n):
    diff = abs(a_n[i] - b_n[i])
    list.append(diff)

if sum(list) > k or (k - sum(list)) % 2 != 0:
    print("No")
