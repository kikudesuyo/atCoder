l = list(map(int, input().split()))
l.sort()

if l[0] + l[1] == l[2]:
    print("Yes")
elif len(set(l)) == 1:
    print("Yes")
else:
    print("No")
