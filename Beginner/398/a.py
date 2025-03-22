n = int(input())

if n % 2 == 0:
    half = n // 2
    print("-" * (half - 1) + "=" * 2 + "-" * (half - 1))
else:
    half = n // 2
    print("-" * half + "=" + "-" * half)
