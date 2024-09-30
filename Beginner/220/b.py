k = int(input())
a, b = input().split()

reversed_a, reversed_b = a[::-1], b[::-1]
int_a, int_b = 0, 0
for i in range(len(a)):
    int_a += int(reversed_a[i]) * (k**i)

for i in range(len(b)):
    int_b += int(reversed_b[i]) * (k**i)


print(int_a * int_b)
