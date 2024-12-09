# 解説AC
# カスタムソートを定義する方法
# -1ならそのまま、1なら入れ替える


from functools import cmp_to_key


def key_func(i, j):
    """
    条件に基づいて2つのインデックスを比較

    2つのリストAとBの要素に基づいて値を計算し比較結果に基づいて-1、1を返す。
    -1のときはそのまま、1のときはiとjを入れ替える。
    """
    diff = A[i] * (A[j] + B[j]) - A[j] * (A[i] + B[i])
    if diff > 0:
        return -1
    elif diff < 0:
        return 1
    else:
        return -1 if i < j else 1


n = int(input())
A, B = [0] * n, [0] * n
for i in range(n):
    A[i], B[i] = map(int, input().split())

ans = list(range(n))
ans.sort(key=cmp_to_key(key_func))

a = [i + 1 for i in ans]
print(*a)
