def judge(s, T):
    t = T.lower()
    initial_t = t[0]
    second_t = t[1]
    end_t = t[2]
    final_flag = False
    if end_t == "x":
        final_flag = True
    initial_count = 100000000000000000
    second_count = 1000000000000
    count = 1
    initial_flag = True
    second_flag = True
    for element in s:
        if (element == initial_t) and initial_flag:
            initial_count = count
            initial_flag = False
        if (element == second_t) and (count > initial_count) and second_flag:
            second_flag = False
            second_count = count
            if final_flag:
                return True
        if (element == end_t) and (count > second_count) and (end_t != "x"):
            return True
        count += 1
    return False


# print(judge("snuke", "RNG"))


s = input()
T = input()

if judge(s, T):
    print("Yes")
else:
    print("No")
