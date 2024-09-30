n = int(input())
s_n, t_n = [], []

for i in range(n):
    s, t = input().split()
    s_n.append(s)
    t_n.append(t)

for i in range(n):
    s_count, t_count = (s_n + t_n).count(s_n[i]), (s_n + t_n).count(t_n[i])
    if s_count >= 2 and t_count >= 2:
        if s_n[i] == t_n[i]:
            continue
        print("No")
        exit()
print("Yes")
