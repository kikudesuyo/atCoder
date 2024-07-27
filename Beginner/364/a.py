n = int(input())
s = [input() for _ in range(n)]
count = 0
for i in range(n - 1):
    if s[i] == "sweet":
        count += 1
    else:
        count = 0
    if count == 2:
        print("No")
        exit()
print("Yes")
