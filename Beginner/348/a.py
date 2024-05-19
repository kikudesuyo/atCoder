n = int(input())


result = ""
for i in range(n):
    if (i + 1) % 3 == 0:
        result += "x"
    else:
        result += "o"

print(result)
