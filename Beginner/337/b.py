s = input()

for i in range(len(s)):
    if i == len(s) - 1:
        break
    if s[i] == "B" and s[i + 1] == "A":
        print("No")
        exit()
    elif s[i] == "C" and (s[i + 1] == "B" or s[i + 1] == "A"):
        print("No")
        exit()
    elif s[i] == "A" and s[i + 1] == "C":
        for j in range(i + 2, len(s)):
            if s[j] == "B":
                print("No")
                exit()

print("Yes")
