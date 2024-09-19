n = int(input())

canditates = []
for i in range(2**n):
    binary = bin(i)[2:].rjust(n, "0")
    elem = binary.replace("0", "(").replace("1", ")")
    count = 0
    for char in elem:
        if count < 0:
            break
        if char == "(":
            count += 1
        if char == ")":
            count -= 1
    if count == 0:
        canditates.append(elem)
print(*canditates, sep="\n")
