n = int(input())


eight_array = []
number = 5
while number < 10**12:
    eight_array.append(number)
    number *= 5

dict = {}
for i, num in enumerate(reversed(eight_array)):
    if n > num:
        dict[len(eight_array) - i] = n // num
        n -= num * (n // num)
    if n < 5:
        dict[0] = 1 + n // 2

# 8ではない0→2→4→6→8と離散的
count = 0
for i in range(len(dict.keys())):
    if i == 0:
        count += i
    else:
        count += int("8" * n)

print(count)
