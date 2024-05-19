str_x = input()
int_x = int(str_x)
if str_x == "0":
    print(0)
    exit()
if str_x[-1] == "0":
    gauss_x = int(str_x[:-1])
else:
    if str_x[0] != "-":
        diff = 10 - int(str_x[-1])
        gauss_x = int(str(int(str_x) + diff)[:-1])
    else:
        if len(str_x) == 2:
            gauss_x = 0
        else:
            diff = int(str_x[-1])
            strip_minus = str_x[1:]
            gauss_x = "-" + str(int(strip_minus) - diff)[:-1]


print(gauss_x)
