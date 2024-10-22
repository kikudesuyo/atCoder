n = int(input())
s = list(input())

set_s = set(s)
s_dict = {}
for i in set_s:
    s_dict[i] = 0

current_char = s[0]
tmp_cnt = 1
for char in s[1:]:
    if current_char != char:
        if s_dict[current_char] < tmp_cnt:
            s_dict[current_char] = tmp_cnt
        current_char = char
        tmp_cnt = 1
    else:
        tmp_cnt += 1
if s_dict[current_char] < tmp_cnt:
    s_dict[current_char] = tmp_cnt


sum = sum(s_dict.values())
print(sum)
