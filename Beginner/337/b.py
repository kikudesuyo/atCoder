s = input()
a_count = s.count("A")
b_count = s.count("B")
c_count = s.count("C")

ideal_string = "A" * a_count + "B" * b_count + "C" * c_count

if s == ideal_string:
    print("Yes")
else:
    print("No")
