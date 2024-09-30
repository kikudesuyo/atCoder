n = int(input())
st_n = [input().split() for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if st_n[i] == st_n[j]:
            print("Yes")
            exit()

print("No")
