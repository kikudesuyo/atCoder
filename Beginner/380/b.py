s = input()

arr = []
cnt = 0
for i in s[1:]:
    if i == "-":
        cnt += 1
    else:
        arr.append(cnt)
        cnt = 0
print(*arr)
