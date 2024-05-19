dict = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


def judge_array(long_string):
    judge_array = []
    for alphabet in dict:
        count = 0
        for s in long_string:
            if alphabet == s:
                count += 1
        judge_array.append(count)
    return judge_array


def is_good_string_on_i(long_string, i):
    array = judge_array(long_string)
    count = 0
    for alphabet_num in array:
        if alphabet_num == i:
            count += 1
    if count == 2 or count == 0:
        return True
    return False


def is_good_string(string):
    for i in range(1, len(string) + 1):
        if not is_good_string_on_i(string, i):
            return False
    return True


if is_good_string(input()):
    print("Yes")
else:
    print("No")
