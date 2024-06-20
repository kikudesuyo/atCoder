n = int(input())
a_s = list(map(int, input().split()))

sum = 0
for i in range(len(a_s)):
    sum += a_s[i]

print(sum * -1)
