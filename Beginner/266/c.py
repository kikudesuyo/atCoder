import math

a_xy = list(map(int, input().split()))
b_xy = list(map(int, input().split()))
c_xy = list(map(int, input().split()))
d_xy = list(map(int, input().split()))

ab_vector = [b_xy[0] - a_xy[0], b_xy[1] - a_xy[1]]
bc_vector = [c_xy[0] - b_xy[0], c_xy[1] - b_xy[1]]
cd_vector = [d_xy[0] - c_xy[0], d_xy[1] - c_xy[1]]
da_vector = [a_xy[0] - d_xy[0], a_xy[1] - d_xy[1]]


def distance(vector):
    return (vector[0] ** 2 + vector[1] ** 2) ** 0.5


cos_abc = (ab_vector[0] * bc_vector[0] + ab_vector[1] * bc_vector[1]) / (distance(ab_vector) * distance(bc_vector))
cos_bcd = (bc_vector[0] * cd_vector[0] + bc_vector[1] * cd_vector[1]) / (distance(bc_vector) * distance(cd_vector))
cos_cda = (cd_vector[0] * da_vector[0] + cd_vector[1] * da_vector[1]) / (distance(cd_vector) * distance(da_vector))
cos_dab = (da_vector[0] * ab_vector[0] + da_vector[1] * ab_vector[1]) / (distance(da_vector) * distance(ab_vector))

abc_degree = math.degrees(math.acos(cos_abc))
bcd_degree = math.degrees(math.acos(cos_bcd))
cda_degree = math.degrees(math.acos(cos_cda))
dab_degree = math.degrees(math.acos(cos_dab))

sum_num = abc_degree + bcd_degree + cda_degree + dab_degree

if 358<=sum_num<=363:
    print('Yes')
else:
    print('No')