from collections import defaultdict

s = input()
t = input()

s_at_cnt = 0
t_at_cnt = 0
for i in range(len(s)):
    if s[i] == "@":
        s_at_cnt += 1
    if t[i] == "@":
        t_at_cnt += 1

filtered_s = [x for x in s if x != "@"]
filtered_t = [x for x in t if x != "@"]

s_dict = defaultdict(int)
t_dict = defaultdict(int)
for elem in filtered_s:
    s_dict[elem] += 1
for elem in filtered_t:
    t_dict[elem] += 1

alphabet = "abcdefghijklmnopqrstuvwxyz"


s_diff_cnt = 0
t_diff_cnt = 0
for elem in alphabet:
    if not elem in ["a", "t", "c", "o", "d", "e", "r"]:
        if s_dict[elem] != t_dict[elem]:
            print("No")
            exit()
    if s_dict[elem] < t_dict[elem]:
        s_diff_cnt += t_dict[elem] - s_dict[elem]
    if s_dict[elem] > t_dict[elem]:
        t_diff_cnt += s_dict[elem] - t_dict[elem]


if s_diff_cnt > s_at_cnt:
    print("No")
    exit()
if t_diff_cnt > t_at_cnt:
    print("No")
    exit()
print("Yes")
