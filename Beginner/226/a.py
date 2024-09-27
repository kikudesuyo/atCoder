x = input()

from decimal import Decimal

d = Decimal(x)

print(d.quantize(Decimal("1."), rounding="ROUND_HALF_UP"))
