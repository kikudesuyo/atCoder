s1, s2, s3 = input(), input(), input()
t = input()


answer = ""
for i in t:
    if i == "1":
        answer += s1
    elif i == "2":
        answer += s2
    else:
        answer += s3
print(answer)
