n, l, r = map(int, input().split())
a_n = list(map(int, input().split()))


answers = []
for i in a_n:
    if i < l:
        answers.append(l)
    elif i > r:
        answers.append(r)
    else:
        answers.append(i)
print(*answers)
