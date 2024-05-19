s = input()
t = input()

s_idx = 0
currect_idxs = []
for i in range(len(t)):
    if s[s_idx] == t[i]:
        currect_idxs.append(str(i + 1))
        s_idx += 1

print(" ".join(currect_idxs))


# 文字列の結合だとタイムアウトになるので注意
