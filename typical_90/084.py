n = int(input())
s = input()

if n == 1:
    print(0)
    exit()


is_circle = s[0] == "o"
cnt = 0
i = 1
flag = False
tmp_cnt = 1
while i < n:
    if is_circle:
        if s[i] == "x":
            cnt += tmp_cnt * (n - i)
            is_circle = False
            tmp_cnt = 0
        else:
            tmp_cnt += 1
            i += 1
    else:
        if s[i] == "o":
            cnt += tmp_cnt * (n - i)
            is_circle = True
            tmp_cnt = 0
        else:
            tmp_cnt += 1
            i += 1
print(cnt)
