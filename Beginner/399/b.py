n = int(input())
p_n = list(map(int, input().split()))
s_p = list(reversed(sorted(p_n)))

ans = []
for i in range(n):
    idx = s_p.index(p_n[i])
    ans.append(idx + 1)

# print(*ans)

for i in range(n):
    print(ans[i])
