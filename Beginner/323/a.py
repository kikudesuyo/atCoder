s = input()

count = 1
for i in s:
    if count % 2 == 0:
        if i != "0":
            print("No")
            exit()
    count += 1
print("Yes")
