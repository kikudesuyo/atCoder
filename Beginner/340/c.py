from functools import cache


@cache
def f(n):
    if n == 1:
        return 0
    # f((n+1)//2)のときに誤解されそうだが、nが奇数のときはn+1が偶数になるので、f((n+1)//2)はf(n//2)の次に呼ばれる
    return f(n // 2) + f((n + 1) // 2) + n


print(f(int(input())))
