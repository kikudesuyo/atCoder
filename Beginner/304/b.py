n = int(input())
if n <= 10**3 - 1:
    print(n)
elif 10**3 <= n <= 10**4 - 1:
    print(str(n)[:-1] + "0")
elif 10**4 <= n <= 10**5 - 1:
    print(str(n)[:-2] + "00")
elif 10**5 <= n <= 10**6 - 1:
    print(str(n)[:-3] + "000")
elif 10**6 <= n <= 10**7 - 1:
    print(str(n)[:-4] + "0000")
elif 10**7 <= n <= 10**8 - 1:
    print(str(n)[:-5] + "00000")
elif 10**8 <= n <= 10**9 - 1:
    print(str(n)[:-6] + "000000")
