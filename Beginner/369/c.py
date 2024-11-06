n = int(input())
a_s = list(map(int, input().split()))

if n == 1:
    print(1)
    exit()
count = 0
flag = False
tmp_cnt = 2
i = 0
while i < n - 1:
    if not flag:  # 1，2項から公差取得
        flag = True
        d = a_s[i + 1] - a_s[i]
        tmp_cnt = 2
        i += 1
        continue
    if a_s[i + 1] - a_s[i] == d:
        tmp_cnt += 1
        i += 1
    else:
        count += int(tmp_cnt * (tmp_cnt + 1) / 2) - 1
        flag = False


count += int(tmp_cnt * (tmp_cnt + 1) / 2)
print(count)
