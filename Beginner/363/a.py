r = input()

if len(r) <= 2:
    print(100 - int(r))
else:
    print(100 - int(r[1:]))
