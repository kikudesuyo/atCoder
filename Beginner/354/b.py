n = int(input())


total = 0
user_names = []
rates = []
for i in range(n):
    s, c = input().split()
    rates.append(int(c))
    user_names.append(s)
    total += int(c)

remainder = total % n
user_names.sort()
for i, rate in enumerate(rates):
    if remainder == i:
        print(user_names[i])
        break
