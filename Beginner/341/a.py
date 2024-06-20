n = int(input())

string = ""
for i in range(2 * n + 1):
    if i % 2 == 0:
        string += "1"
    else:
        string += "0"

print(string)
