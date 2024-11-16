n, k = map(int, input().split())
s = input()


arr = []
flag = False
for i in range(n):
    if not flag and s[i] == "1":
        flag = True
        start_idx = i
    if s[i] == "0" and flag:
        flag = False
        arr.append((start_idx, int(i) - 1))
if flag:
    arr.append((start_idx, n - 1))


ans = []
i = 0
diff = arr[k - 1][1] - arr[k - 1][0] + 1
while len(ans) < n:
    if i < arr[k - 2][1]:
        ans.append(s[i])
    elif arr[k - 2][1] < i <= arr[k - 2][1] + diff:
        ans.append("1")
    elif arr[k - 1][0] <= i <= arr[k - 1][1]:
        ans.append("0")
    else:
        ans.append(s[i])
    i += 1


print("".join(ans))
