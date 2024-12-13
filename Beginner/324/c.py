str_n, str_t_dash = input().split()
n = int(str_n)
t_dash = list(str_t_dash)

s_n = [list(input()) for _ in range(n)]


def step1(s, t_dash):
    return s == t_dash


def step2(s, t_dash):
    s_i, t_i = 0, 0
    while s_i < len(s) and t_i < len(t_dash):
        if s[s_i] == t_dash[t_i]:
            s_i += 1
            t_i += 1
        else:
            t_i += 1
    if s_i == len(s):
        return True
    return False


def step4(s, t_dash):
    cnt = 0
    for i in range(len(s)):
        if s[i] != t_dash[i]:
            cnt += 1
    return cnt == 1


def step3(s, t_dash):
    s_i, t_i = 0, 0
    while s_i < len(s) and t_i < len(t_dash):
        if s[s_i] == t_dash[t_i]:
            s_i += 1
            t_i += 1
        else:
            s_i += 1
    if t_i == len(t_dash):
        return True
    return False


ans = []
for i, original in enumerate(s_n):
    if len(original) == len(t_dash):  # 同じとき
        if step1(original, t_dash):
            ans.append(i + 1)
            continue
        cnt = 0
        if step4(original, t_dash):
            ans.append(i + 1)
            continue
    elif len(original) + 1 == len(t_dash):  # 挿入
        if step2(original, t_dash):
            ans.append(i + 1)
            continue
    elif len(original) == len(t_dash) + 1:  # 削除
        if step3(original, t_dash):
            ans.append(i + 1)
            continue

if len(ans) == 0:
    print(0)
else:
    print(len(ans))
    print(*ans)
