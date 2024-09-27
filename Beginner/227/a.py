n, k, a = map(int, input().split())
idx = (k % n) - 1
arr = []
reminder = []
for i in range(1, n + 1):
    if i < a:
        reminder.append(i)
    else:
        arr.append(i)

arr = arr + reminder
print(arr[idx])
