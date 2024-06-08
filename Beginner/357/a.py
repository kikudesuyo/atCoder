n, m = map(int, input().split())
h_s = list(map(int, input().split()))

left_m = m
for i in range(n):
    if left_m < h_s[i]:
        print(i)
        exit()
    left_m -= h_s[i]
print(n)
