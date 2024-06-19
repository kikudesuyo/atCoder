s = input()


first_str = ""
another_str = ""
for i in range(len(s)):
    if i == 0:
        first_str = s[i]
    elif first_str != s[i]:
        another_str = s[i]
        break
is_first_str_multiple = True
for i in range(1, len(s)):
    if s[i] == first_str:
        is_first_str_multiple = False
        break

if is_first_str_multiple:
    print(1)
    exit()

for i in range(1, len(s)):
    if s[i] == another_str:
        print(i + 1)
        break
