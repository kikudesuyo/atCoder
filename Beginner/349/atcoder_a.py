def judge(N, A_string):
    A_array = A_string.split(" ")
    a_int_array = list(map(int, A_array))
    count = 0
    for i in a_int_array:
        count += i
    print(int(N) - count)


string = input()
array = input()

judge(string, array)
