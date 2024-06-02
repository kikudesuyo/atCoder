n, m = map(int, input().split())
a_s = list(map(int, input().split()))

x_dict = {}
for i in range(1, n + 1):
    x_col = list(map(int, input().split()))
    for j in range(1, m + 1):
        if j not in x_dict:
            x_dict[j] = []
        x_dict[j].append(x_col[j - 1])

for i in range(1, m + 1):
    arr = x_dict[i]
    if sum(arr) < a_s[i - 1]:
        print("No")
        exit()

print("Yes")
