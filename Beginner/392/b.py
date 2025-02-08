n, m = map(int, input().split())
a_m = list(map(int, input().split()))

ans = []
for i in range(1, n + 1):
    if i not in a_m:
        ans.append(i)

if len(ans) == 0:
    print(0)
    print()
else:
    print(len(ans))
    print(*ans)
