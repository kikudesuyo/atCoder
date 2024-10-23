s1, s2, s3 = input().split()
t1, t2, t3 = input().split()

cnt = 0
if s1 == t1:
    cnt += 1
if s2 == t2:
    cnt += 1
if s3 == t3:
    cnt += 1

if cnt in [0, 3]:
    print("Yes")
else:
    print("No")
