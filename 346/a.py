n = int(input())
a_s = list(map(int, input().split()))

b_s = ""
for i in range(n - 1):
    b_s += str(a_s[i] * a_s[i + 1]) + " "

print(b_s)
