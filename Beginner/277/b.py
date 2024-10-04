n = int(input())
s_n = [input() for _ in range(n)]

first_chars = ["H", "D", "C", "S"]
second_chars = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]


for f, s in s_n:
    if not (f in first_chars and s in second_chars):
        print("No")
        exit()

if len(set(s_n)) != n:
    print("No")
    exit()
print("Yes")
