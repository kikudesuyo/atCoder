k = int(input())
s = list(input())
t = list(input())

if abs(len(s) - len(t)) > k:
    print("No")
    exit()


if len(s) == len(t):
    cnt = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            cnt += 1
    if cnt <= k:
        print("Yes")
    else:
        print("No")
    exit()


if len(s) < len(t):
    small_str, large_str = s, t
elif len(s) > len(t):
    small_str, large_str = t, s

s_idx = 0
l_idx = 0
diff_cnt = 0

while l_idx < len(large_str) and s_idx < len(small_str):
    if small_str[s_idx] == large_str[l_idx]:
        s_idx += 1
        l_idx += 1
    else:
        l_idx += 1
        diff_cnt += 1


if diff_cnt <= 1:
    print("Yes")
else:
    print("No")
