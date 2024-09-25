n = int(input())
ans = 100
temp = 5
for i in range(1, 100 + 1):
    if i % 5 == 0:
        abs_num = abs(i - n)
        print(i, abs_num)
        if abs_num < temp:
            temp = abs_num
            ans = i
print(ans)
