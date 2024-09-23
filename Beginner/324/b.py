max_x = 60
min_y = 60

n = int(input())

for i in range(max_x):
    for j in range(min_y):
        if n == (2**i) * (3**j):
            print("Yes")
            exit()
print("No")
