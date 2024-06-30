s, t = input().split()

# i文字で区切る
for i in range(1, len(s)):
    idx_dict = {}
    splited_strs = [s[j : j + i] for j in range(0, len(s), i)]
    for elem in splited_strs:
        for j in range(len(elem)):
            if not j in idx_dict:
                idx_dict[j] = elem[j]
            else:
                idx_dict[j] += elem[j]
    for value in idx_dict.values():
        if t == value:
            print("Yes")
            exit()

print("No")
