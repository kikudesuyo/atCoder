s = input()

dict = {}
for i in range(len(s)):
    if s[i] in dict:
        dict[s[i]] += 1
    else:
        dict[s[i]] = 1

max_num = 0
max_str = ""
for key in dict:
    if dict[key] > max_num:
        max_num, max_str = dict[key], key
    if dict[key] == max_num:
        # 辞書が小さい方に更新
        if max_str > key:
            max_str = key
print(max_str)
