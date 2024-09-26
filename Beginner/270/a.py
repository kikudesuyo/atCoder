a, b = map(int, input().split())


def output(a):
    a_list = []
    if a == 0:
        a_list = []
    elif a == 1:
        a_list = [1]
    elif a == 2:
        a_list = [2]
    elif a == 3:
        a_list = [2, 1]
    elif a == 4:
        a_list = [4]
    elif a == 5:
        a_list = [1, 4]
    elif a == 6:
        a_list = [2, 4]
    elif a == 7:
        a_list = [4, 2, 1]
    return a_list


a, b = output(a), output(b)
sunuke = list(set(a) | set(b))
print(sum(sunuke))
