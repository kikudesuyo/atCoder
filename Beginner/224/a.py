s = input()

if len(s) == 2:
    if s == "er":
        print("er")
else:
    if s[-2:] == "er":
        print("er")
    else:
        print("ist")
