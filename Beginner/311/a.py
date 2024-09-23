n = int(input())
s = input()

is_a = False
is_b = False
is_c = False

for i in range(n):
    if s[i] == "A":
        is_a = True
    if s[i] == "B":
        is_b = True
    if s[i] == "C":
        is_c = True
    if is_a and is_b and is_c:
        print(i + 1)
        break
