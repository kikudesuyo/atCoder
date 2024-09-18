n = int(input())
s = input()

for i in range(len(s)):
    if i + 1 >= len(s):
        break
    if s[i : i + 2] == "ab":
        print("Yes")
        exit()
    if s[i : i + 2] == "ba":
        print("Yes")
        exit()


print("No")
