n = int(input())
a_nn = [input() for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            if a_nn[i][j] != "-":
                print("incorrect")
                exit()
        if a_nn[i][j] == "L":
            if a_nn[j][i] != "W":
                print("incorrect")
                exit()
        if a_nn[i][j] == "W":
            if a_nn[j][i] != "L":
                print("incorrect")
                exit()
        if a_nn[i][j] == "D":
            if a_nn[j][i] != "D":
                print("incorrect")
                exit()
print("correct")
