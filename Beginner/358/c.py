# import itertools

# n, m = map(int, input().split())
# s_s = []
# for i in range(n):
#     s_s.append(input())

# result = m
# popcorns = ["x"] * m
# store_count = 0
# count_flag = False
# round_robin_s_s = list((itertools.permutations(s_s)))
# round_robin_s_s = [list(s) for s in round_robin_s_s]


# for s in range(len(round_robin_s_s)):
#     for i in range(n):
#         for j in range(m):
#             if round_robin_s_s[s][i][j] == "o" and popcorns[j] == "x":
#                 popcorns[j] = "o"
#                 count_flag = True
#         if count_flag:
#             store_count += 1
#             count_flag = False
#         if popcorns.count("o") == m:
#             if store_count < result:
#                 result = store_count
#     store_count = 0
#     popcorns = ["x"] * m

# print(result)


n, m = map(int, input().split())
s_s = []
for i in range(n):
    s_s.append(input())

strip_idxes = []
stripped_s_s = s_s.copy()
for r in range(len(s_s)):
    my_store = s_s[r]
    for i in range(len(s_s)):
        if i == r:
            continue
        oppnent_store = s_s[i]
        number_of_opponent = 0
        for j in range(m):
            if my_store[j] == "o" and oppnent_store[j] == "x":
                number_of_opponent = 0
                break
            if oppnent_store[j] == "o":
                number_of_opponent += 1
        if number_of_opponent > my_store.count("o"):
            strip_idxes.append(r)
            break

for i in sorted(strip_idxes, reverse=True):
    stripped_s_s.pop(i)


import itertools

result = m
popcorns = ["x"] * m
store_count = 0
count_flag = False
round_robin_s_s = list((itertools.permutations(stripped_s_s)))
round_robin_s_s = [list(s) for s in round_robin_s_s]


for s in range(len(round_robin_s_s)):
    for i in range(n):
        for j in range(m):
            if round_robin_s_s[s][i][j] == "o" and popcorns[j] == "x":
                popcorns[j] = "o"
                count_flag = True
        if count_flag:
            store_count += 1
            count_flag = False
        if popcorns.count("o") == m:
            if store_count < result:
                result = store_count
    store_count = 0
    popcorns = ["x"] * m
print(result)
