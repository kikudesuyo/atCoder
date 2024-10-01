n = int(input())
divisors = []
for i in range(1, n + 1):
    if n % i == 0:
        if i <= 9:
            divisors.append(i)
answer = ""
for i in range(0, n + 1):
    min_num = 10
    for divisor in divisors:
        if i % int(n // divisor) == 0:
            min_num = min(min_num, divisor)
    if min_num == 10:
        answer += "-"
    else:
        answer += str(min_num)
print(answer)
