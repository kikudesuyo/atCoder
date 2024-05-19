### わからーん
input = input()
str_l, str_r = input.split()
l, r = int(str_l), int(str_r)


def default():
    i = 0
    power = 0
    array = []
    first_flag = True
    while True:
        power = 2**i
        # 最後
        if power * 2 >= r:
            array.append([power, r - 1])
            array.append([r - 1, r])
            break
        # 基本
        if not first_flag:
            array.append([power, power * 2])
        # 最初
        if first_flag:
            if l <= power:
                array.append([l, power])
                if power * 2 >= r:
                    array.append([power, r - 1])
                    array.append([r - 1, r])
                    break
                else:
                    array.append([power, power * 2])
                first_flag = False
        i += 1

    return array


if l == 0:
    print(1)
    print(0, l)
else:
    array = default()
    print(len(array))
    for i in range(len(array)):
        print(array[i][0], array[i][1])
