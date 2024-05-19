n, k = list(map(int, input().split()))
a_s = list(map(int, input().split()))
count = 1
total_passengers = 0
for i in range(len(a_s)):
    if total_passengers + a_s[i] > k:
        count += 1
        total_passengers = 0
    total_passengers += a_s[i]
print(count)
