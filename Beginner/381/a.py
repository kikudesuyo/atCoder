n = int(input())

s = list(input())

if len(s) % 2 != 1:
    print("No")
    exit()

middle_index = len(s) // 2


if s[:middle_index] != ["1"] * middle_index:
    print("No")
    exit()
if s[middle_index] != "/":
    print("No")
    exit()

if s[middle_index + 1 :] != ["2"] * middle_index:
    print("No")
    exit()

print("Yes")
