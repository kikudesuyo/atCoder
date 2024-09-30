n = int(input())
s_n = list(map(int, input().split()))


count = n
flag = False
for s in s_n:
    for a in range(1, 200):
        if flag:
            flag = False
            break
        for b in range(1, 200):
            area = 4 * a * b + 3 * a + 3 * b
            if area == s:
                count -= 1
                flag = True
                break


print(count)
