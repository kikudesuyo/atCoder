s = input()
ansewr = ""
for i in range(len(s)):
    if s[i] == "0":
        ansewr += "1"
    else:
        ansewr += "0"

print(ansewr)
