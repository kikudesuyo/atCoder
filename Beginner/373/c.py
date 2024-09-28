n = int(input())

a_n = list(map(int, input().split()))
b_n = list(map(int, input().split()))

sorted_a_n = sorted(a_n, reverse=True)
sorted_b_n = sorted(b_n, reverse=True)

print(sorted_a_n[0] + sorted_b_n[0])
