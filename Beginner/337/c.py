n = int(input())
a_s = list(map(int, input().split()))


idx_dict = {}
for i in range(len(a_s)):
    idx_dict[a_s[i]] = i + 1


strings = []
temp_idx = None
for i in range(len(idx_dict.keys())):
    if i == 0:
        strings.append(str(idx_dict[-1]))
        temp_idx = idx_dict[-1]
        continue
    strings.append(str(idx_dict[temp_idx]))
    temp_idx = idx_dict[temp_idx]

print(*strings)
