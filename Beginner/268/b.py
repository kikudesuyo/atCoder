s = input()
t = input()
if len(s) > len(t):
    print("No")
    exit()
for idx in range(len(s)):
    if s[idx] != t[idx]:
        print("No")
        exit()
print("Yes")
