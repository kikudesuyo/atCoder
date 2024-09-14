n, m = map(int, input().split())

male_list = [False] * n

for i in range(m):
    a, b = input().split()
    if b == "M":
        if not male_list[int(a) - 1]:
            print("Yes")
            male_list[int(a) - 1] = True
        else:
            print("No")
    else:
        print("No")
