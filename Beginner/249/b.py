s = input()

is_lower = False
is_upper = False
for i in range(len(s)):
    if s[i].islower():
        is_lower = True
    if s[i].isupper():
        is_upper = True

if len(set(s)) == len(s) and is_lower and is_upper:
    print("Yes")
else:
    print("No")
