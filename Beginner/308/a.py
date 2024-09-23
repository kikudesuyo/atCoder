s_s = list(map(int, input().split()))

if not (min(s_s) >= 100 and max(s_s) <= 675):
    print("No")
    exit()

sorted_s_s = sorted(s_s)
if sorted_s_s != s_s:
    print("No")
    exit()

for i in s_s:
    if i % 25 != 0:
        print("No")
        exit()
print("Yes")
