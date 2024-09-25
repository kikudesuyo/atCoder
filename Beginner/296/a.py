n = int(input())
s = input()

male_count = s.count("MM")
female_count = s.count("FF")
if male_count == 0 and female_count == 0:
    print("Yes")
else:
    print("No")
