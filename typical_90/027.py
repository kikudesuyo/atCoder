from bisect import bisect_left, bisect_right

n = int(input())
s_n = [input() for _ in range(n)]


users = list(set(s_n))
dict_users = {}
for i in range(len(users)):
    dict_users[users[i]] = False


for i in range(n):
    if dict_users[s_n[i]] == False:
        dict_users[s_n[i]] = True
        print(i + 1)
