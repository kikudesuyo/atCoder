s = input()

first_idx = 0
second_idx = 0

first_flag = False
for i in range(len(s)):
    if s[i] == "|" and not first_flag:
        first_idx = i
        first_flag = True
        continue
    if first_flag:
        if s[i] == "|":
            second_idx = i
            break

print(s[:first_idx] + s[second_idx + 1 :])
