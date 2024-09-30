a, b = input().split()

reversed_a, reversed_b = a[::-1], b[::-1]


min_length = min(len(a), len(b))

for i in range(min_length):
    if int(reversed_a[i]) + int(reversed_b[i]) >= 10:
        print("Hard")
        exit()
print("Easy")
