s = input()

answer = ""
for i in range(len(s)):
    if i % 2 == 0:
        answer += s[i + 1]
    else:
        answer += s[i - 1]
print(answer)
