n, k = list(map(int, input().split()))
a_list = list(map(int, input().split()))
divisions = ""
for i in range(n):
    if a_list[i] % k == 0:
        divisions += f"{a_list[i]//k} "

print(divisions)
