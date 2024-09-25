n = int(input())
s = input()

good_count = s.count("o")
bad_count = s.count("x")
if good_count > 0 and bad_count == 0:
    print("Yes")
else:
    print("No")
