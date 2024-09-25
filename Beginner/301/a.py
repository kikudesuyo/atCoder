n = int(input())
s = input()

t_count, a_count = 0, 0
half = n // 2
for i in range(n):
    if s[i] == "T":
        t_count += 1
    else:
        a_count += 1
    if n % 2 == 0:
        if t_count >= half:
            print("T")
            exit()
        elif a_count >= half:
            print("A")
            exit()

if t_count > a_count:
    print("T")
else:
    print("A")
