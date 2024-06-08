s = input()

upper = 0
lower = 0
for i in range(len(s)):
    if s[i].islower():
        lower += 1
    else:
        upper += 1

if upper > lower:
    print(s.upper())
else:
    print(s.lower())
