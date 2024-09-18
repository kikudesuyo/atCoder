b = int(input())


for i in range(1, 22):
    if b == i**i:
        print(i)
        exit()
print(-1)
