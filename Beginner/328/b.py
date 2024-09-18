n = int(input())
d_s = list(map(int, input().split()))

month = 1
count = 0
for d in d_s:
    for i in range(1, d + 1):
        string = len(set(str(month) + str(i)))
        if string == 1:
            count += 1
    month += 1
print(count)
