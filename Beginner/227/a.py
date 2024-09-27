n, k, a = map(int, input().split())
idx = k % 3
arr = []
for i in range(n):
    if i <= n - a:
        arr.append(a + i)
    else:
        arr.append(i - a + 1)
print(arr[idx - 1])
