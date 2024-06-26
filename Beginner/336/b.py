n = int(input())

binary = bin(n)[2:]

count = 0
for i in reversed(range(len(binary))):
    if binary[i] == "1":
        print(count)
        exit()
    count += 1
