import string

n, s, q = int(input()), input(), int(input())
alphatbet_str = string.ascii_lowercase
changed_str = string.ascii_lowercase
for i in range(q):
    c, d = input().split()
    changed_str = changed_str.replace(c, d)
print(s.translate(str.maketrans(alphatbet_str, changed_str)))
