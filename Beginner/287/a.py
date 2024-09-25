n = int(input())
s_s = [input() for _ in range(n)]
against_count = s_s.count("Against")
approve_count = s_s.count("For")
if against_count > approve_count:
    print("No")
else:
    print("Yes")
