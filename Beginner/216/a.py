hoge = input()

x = int(float(hoge))
y = int(hoge[-1])

if y <= 2:
    print(str(x) + "-")
elif y <= 6:
    print(x)
else:
    print(str(x) + "+")
