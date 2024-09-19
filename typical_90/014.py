n = int(input())
a_n = list(map(int, input().split()))
b_n = list(map(int, input().split()))


sorted_a_n = sorted(a_n)
sorted_b_n = sorted(b_n)

sum = 0
for idx in range(n):
    sum += abs(sorted_a_n[idx] - sorted_b_n[idx])
print(sum)
