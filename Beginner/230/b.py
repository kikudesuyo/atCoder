s = input()

t = "oxx" * 10**5

candicates = ["oxxoxxoxxo", "xxoxxoxxox", "xoxxoxxoxx"]

for candicate in candicates:
    if s in candicate:
        print("Yes")
        exit()
print("No")
