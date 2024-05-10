s = list(input())

# alphabets = "abcdefghijklmnopqrstuvwxyz"
# dict = {}
# for i in alphabets:
#     dict[i] = s.count(i)

count = 0
for i in range(0, len(s) - 1):
    s[i:]
if count == 0:
    print(1)
else:
    print(count)


# count = 0
# for i in range(len(s) - 1):
#     for j in range(i, len(s)):
#         # print(s[i], s[j])
#         if s[i] == s[j]:
#             continue
#         else:
#             count += 1
# if count == 0:
#     print(1)
# else:
#     print(count)
