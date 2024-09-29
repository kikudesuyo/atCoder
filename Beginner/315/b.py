m = int(input())
d_n = list(map(int, input().split()))

middle_day = sum(d_n) // 2 + 1

temp_day = 0
for i in range(m):
    if temp_day + d_n[i] >= middle_day:
        reminder = middle_day - temp_day
        print(i + 1, reminder)
        break
    else:
        temp_day += d_n[i]
