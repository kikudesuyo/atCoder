s, t = input(), input()

diff_idx = -1
for i in range(len(s)):
    if s[i] != t[i]:
        diff_idx = i
        break

if diff_idx == -1:
    print("Yes")
    exit()
if diff_idx == len(s) - 1:
    print("No")
    exit()

s_str, t_str = s[diff_idx], t[diff_idx]
next_s, next_t = s[diff_idx + 1], t[diff_idx + 1]

if s_str == next_t and t_str == next_s:
    print("Yes")
else:
    print("No")
