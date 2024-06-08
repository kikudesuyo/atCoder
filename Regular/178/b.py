t = int(input())

test_cases = []
for i in range(t):
    a_s = list(map(int, input().split()))
    test_cases.append(a_s)

divided_num = 998244353


for test_case in test_cases:
    x_1, x_2, x_3 = test_case
    if x_1 > x_2:
        big_digit_num = x_1
        small_digit_num = x_2
    else:
        big_digit_num = x_2
        small_digit_num = x_1
    if x_3 != big_digit_num or x_3 != big_digit_num + 1:
        print(0)
