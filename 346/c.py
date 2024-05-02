n, k = list(map(int, input().split()))
a_s = list(map(int, input().split()))

striped_a = []
for i in list(set(a_s)):
    if i <= k:
        striped_a.append(i)

sum_a = sum(striped_a)
sum_k = (k * (1 + k)) // 2
print(sum_k - sum_a)
