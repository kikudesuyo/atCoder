a, b = map(int, input().split())


b_num, s_num = max(a, b), min(a, b)

cnt = 0
while b_num % s_num != 0:
    cnt += b_num // s_num
    q, r = divmod(b_num, s_num)
    b_num, s_num = s_num, r


cnt += b_num // s_num - 1
print(cnt)
