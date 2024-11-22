n = int(input())

s = input()

ans = 1
i = 0
flag_1 = False
flag_slash = False
while i < n:
    one_count = 0
    while s[i] == "1":
        flag_1 = True
        one_count += 1
        i += 1
        if i == n:
            break
    if i == n:
        break

    if flag_1 and s[i] == "/":
        flag_slash = True
        i += 1
    else:
        flag_1 = False
        i += 1
        continue
    if i == n:
        break
    if flag_1 and flag_slash and s[i] == "2":
        two_count = 0
        while s[i] == "2":
            two_count += 1
            i += 1
            if i == n:
                break
        ans = max(ans, min(one_count, two_count) * 2 + 1)
        flag_1 = False
        flag_slash = False
    else:
        flag_1 = False
        flag_slash = False


print(ans)
