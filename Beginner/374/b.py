s = input()
t = input()

if s == t:
    print(0)
    exit()

count = 1
min_num = min(len(s), len(t))
for i in range(min_num):
    if s[i] == t[i]:
        count += 1
    else:
        print(count)
        exit()
print(count)
exit()
