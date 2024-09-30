n = int(input())
a_n = list(map(int, input().split()))
sorted_a_n = sorted(a_n, reverse=True)
for i in range(n - 1):
    if sorted_a_n[i * 4] != sorted_a_n[i * 4 + 3]:
        print(sorted_a_n[i * 4])
        exit()
print(1)
