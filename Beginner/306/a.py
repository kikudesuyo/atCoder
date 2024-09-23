n = int(input())
s = input()
answer = ""
for i in range(len(s)):
    answer += s[i] + s[i]
print(answer)
