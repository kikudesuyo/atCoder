n = int(input())
a_nn = [list(map(int, input().split())) for _ in range(n)]
b_nn = [list(map(int, input().split())) for _ in range(n)]

one_idxes = []
for i in range(n):
    for j in range(n):
        if a_nn[i][j] == 1:
            one_idxes.append((i, j))


# 0度回転
flag = True
for i in range(len(one_idxes)):
    if not b_nn[one_idxes[i][0]][one_idxes[i][1]] == 1:
        flag = False
        break
if flag:
    print("Yes")
    exit()

r_b_nn = []
for i in range(n):
    tmp = []
    for j in range(n):
        tmp.append(b_nn[n - 1 - j][i])
    r_b_nn.append(tmp)

# 90度回転
flag = True
for i in range(len(one_idxes)):
    if not r_b_nn[one_idxes[i][0]][one_idxes[i][1]] == 1:
        flag = False
        break
if flag:
    print("Yes")
    exit()


r2_b_nn = []
for i in range(n):
    tmp = []
    for j in range(n):
        tmp.append(r_b_nn[n - 1 - j][i])
    r2_b_nn.append(tmp)

flag = True
for i in range(len(one_idxes)):
    if not r2_b_nn[one_idxes[i][0]][one_idxes[i][1]] == 1:
        flag = False
        break
if flag:
    print("Yes")
    exit()

r3_b_nn = []
for i in range(n):
    tmp = []
    for j in range(n):
        tmp.append(r2_b_nn[n - 1 - j][i])
    r3_b_nn.append(tmp)
flag = True
for i in range(len(one_idxes)):
    if not r3_b_nn[one_idxes[i][0]][one_idxes[i][1]] == 1:
        flag = False
        break
if flag:
    print("Yes")
    exit()
print("No")
