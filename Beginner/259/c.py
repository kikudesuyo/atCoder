s = list(input())
t = list(input())

if len(s) > len(t):
    print("No")
    exit()

s_idx = 0
t_idx = 0
while s_idx < len(s) and t_idx < len(t):
    if s[s_idx] != t[t_idx]:
        print("No")
        exit()
    s_cnt = 1
    t_cnt = 1
    while s_idx < len(s) - 1:  # sに対するループ
        if s[s_idx] == s[s_idx + 1]:
            s_cnt += 1
            s_idx += 1
        else:
            break
    while t_idx < len(t) - 1:
        if t[t_idx] == t[t_idx + 1]:
            t_cnt += 1
            t_idx += 1
        else:
            break
    if s_cnt == t_cnt:
        s_idx += 1
        t_idx += 1
    else:
        if s_cnt > t_cnt or s_cnt == 1:
            print("No")
            exit()

if s_idx < len(s) - 1 or t_idx < len(t) - 1:
    print("No")
    exit()
print("Yes")
