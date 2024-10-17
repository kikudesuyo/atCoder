n, w = map(int, input().split())
ab_list = [list(map(int, input().split())) for _ in range(n)]

yammy_sort = sorted(ab_list, key=lambda x: x[0], reverse=True)

ans = 0
for i in range(n):
    if w > yammy_sort[i][1]:
        w -= yammy_sort[i][1]
        ans += yammy_sort[i][0] * yammy_sort[i][1]
    else:
        ans += yammy_sort[i][0] * w
        break
print(ans)
