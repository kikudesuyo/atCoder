n = list(input())

temp = 10
for i in n:
    if temp <= int(i):
        print("No")
        exit()
    temp = int(i)

print("Yes")
