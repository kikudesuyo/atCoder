n = int(input())
s = input()

start_idx = 0
separeted_s = []
idx = 0
for j in range(len(s)):
    if s[idx : idx + 2] == "AA" or s[idx : idx + 2] == "BB":
        separeted_s.append(s[start_idx : idx + 1])
        start_idx = idx + 1
        idx += 1
    else:
        idx += 1
    if j == len(s) - 1:
        separeted_s.append(s[start_idx : idx + 1])
separeted_s_length = []
for elem in separeted_s:
    separeted_s_length.append(-(-len(elem) // 2))
arr_idx = 0
striped_s = []
for i in range(len(separeted_s_length)):
    if separeted_s_length[i] != 0:
        striped_s.append(separeted_s_length[i])
count = 1
for i in range(len(striped_s)):
    count *= striped_s[i]
print(count % (10**9 + 7))
