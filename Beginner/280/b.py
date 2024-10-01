n = int(input())
s_n = list(map(int, input().split()))

ans = []
sum = 0
for i in s_n:
    ans.append(i - sum)
    sum += i - sum

print(*ans)
