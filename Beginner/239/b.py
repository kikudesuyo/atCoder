x = input()

if x[0] == "-":
    if len(x) == 2:
        print(-1)
        exit()
    elif x[-1] == "0":
        answer = int(x[:-1])
    else:
        answer = int(x[:-1]) - 1
else:
    if len(x) == 1:
        answer = 0
    else:
        answer = x[:-1]
print(answer)
