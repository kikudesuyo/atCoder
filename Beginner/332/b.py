k, g, m = map(int, input().split())

glass, cup = 0, 0
for i in range(k):
    if glass == g:
        glass = 0
    elif cup == 0:
        cup = m
    else:
        if cup > g - glass:
            cup -= g - glass
            glass += g - glass
        else:
            glass += cup
            cup = 0

print(glass, cup)
