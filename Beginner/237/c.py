s = input()

f = True
strip_a_s = []
h_cnt = 0
for i in range(len(s)):  # 先頭のa削除
    if f:
        if s[i] != "a":
            strip_a_s.append(s[i])
            f = False
        else:
            h_cnt += 1
    else:
        strip_a_s.append(s[i])

l_cnt = 0
for i in reversed(range(len(strip_a_s))):  # 末尾のa削除
    if strip_a_s[i] == "a":
        strip_a_s.pop()
        l_cnt += 1
    else:
        break

if strip_a_s == []:
    print("Yes")
    exit()

if strip_a_s == strip_a_s[::-1] and h_cnt <= l_cnt:
    print("Yes")
else:
    print("No")
