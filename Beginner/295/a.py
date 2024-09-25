n = int(input())
w_n = input().split()

list = ["and", "not", "that", "the", "you"]
for i in w_n:
    if i in list:
        print("Yes")
        exit()
print("No")
