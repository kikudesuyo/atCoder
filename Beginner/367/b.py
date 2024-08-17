str_x = input()

reversed_str_x = str_x[::-1]


idx = 0
for i in reversed_str_x:
    if i != "0":
        break
    idx += 1


str_x = reversed_str_x[idx:][::-1]
if str_x[-1] == ".":
    print(str_x[:-1])
else:
    print(str_x)
