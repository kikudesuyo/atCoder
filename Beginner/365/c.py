n, m = map(int, input().split())
a_s = list(map(int, input().split()))

sorted_a = sorted(a_s)

if sum(a_s) <= m:
    print("infinite")
    exit()

left_length = n
count = 0
times = 0
for i in range(n):
    if sorted_a[i] == times:
        left_length -= 1
        continue
    if (sorted_a[i] - times) * left_length + count < m:
        count += (sorted_a[i] - times) * left_length
        times += sorted_a[i] - times
        left_length -= 1
        continue

    else:
        print(times + (m - count) // left_length)
        exit()
