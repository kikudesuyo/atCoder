import math

n, a, b = map(int, input().split())

sum_num = (1 + n) * n // 2

a_cnt = n // a
b_cnt = n // b
ab_lcm = a * b // math.gcd(a, b)
ab_cnt = n // ab_lcm
a_sum_num = (a + a * a_cnt) * a_cnt // 2
b_sum_num = (b + b * b_cnt) * b_cnt // 2
ab_lcm_sum_num = (ab_lcm + ab_lcm * ab_cnt) * ab_cnt // 2

print(sum_num - a_sum_num - b_sum_num + ab_lcm_sum_num)
