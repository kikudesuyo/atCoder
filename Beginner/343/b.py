n = int(input())

arr = []
for i in range(n):
    row = list(map(int, input().split()))
    outputs = []
    for idx in range(len(row)):
        if row[idx] == 1:
            outputs.append(idx + 1)
    print(*outputs, sep=" ")
