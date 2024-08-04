t = int(input())
t_s = []
for i in range(t):
    n = int(input())
    p_n = list(map(int, input().split()))
    t_s.append((n, p_n))

for p_length, p_s in t_s:
    zero_arr = [i + 1 for i in range(p_length)]
    if p_s == zero_arr:
        print(0)
        continue
    one_flag = False
    max_num = 0
    for i in range(p_length):
        max_num = max(max_num, p_s[i])
        if p_s[i] == i + 1:
            if max_num == i + 1:
                one_flag = True
                break
    if one_flag:
        print(1)
    else:
        if p_s[-1] == 1 and p_s[0] == p_length:
            print(3)
        else:
            print(2)
