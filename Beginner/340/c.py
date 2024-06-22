n = int(input())
sum_num = 0

one_count, other_count = 1, 0
one_number, other_number = n, None
while True:
    if other_number is None:
        if one_number == 1:
            break
        if one_number % 2 == 0:
            sum_num += one_number * one_count
            one_count *= 2
            one_number = one_number // 2
        else:
            sum_num += one_count * one_number
            other_number = one_number // 2 + 1
            one_number = one_number // 2
            other_count = one_count
        continue
    if one_number % 2 == 0:
        sum_num = sum_num + one_count * one_number + other_count * other_number
        one_count = one_count * 2 + other_count
        one_number = one_number // 2
        other_number = other_number // 2 + 1
    else:
        if one_number == 1:
            sum_num = sum_num + other_count * other_number
            break
        sum_num = sum_num + one_count * one_number + other_count * other_number
        other_count = other_count * 2 + one_count
        one_number = one_number // 2
        other_number = other_number // 2
print(sum_num)
