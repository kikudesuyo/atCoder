n = int(input())

a = []
b = []
for i in range(n):
    a_elem = list(input())
    a.append(a_elem)
for i in range(n):
    b_elem = list(input())
    b.append(b_elem)

for i in range(n):
    for j in range(n):
        if a[i][j] != b[i][j]:
            print(f"{i+1} {j+1}")
