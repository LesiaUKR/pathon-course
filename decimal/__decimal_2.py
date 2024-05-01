# rounding
import decimal
from decimal import Decimal, ROUND_HALF_EVEN, ROUND_HALF_UP, ROUND_DOWN

num = Decimal("1.45")
print(num.quantize(Decimal("1.0"), rounding=ROUND_HALF_EVEN))

num = Decimal("1.45")
print(num.quantize(Decimal("1.0"), rounding=ROUND_HALF_UP))

print(Decimal("3.14159").quantize((Decimal("1.000"))))

r_num = (Decimal("11") / Decimal("3")).quantize((Decimal("1.000000")))
print(r_num)

# Вихідне число Decimal
number = Decimal('3.14159')

# Встановлення точності до двох знаків після коми
rounded_number = number.quantize(Decimal('0.00'), rounding=ROUND_DOWN)  # 3.14

print(rounded_number)

number = Decimal("1.45")

# Округлення за замовчуванням до одного десяткового знаку
print("Округлення за замовчуванням ROUND_HALF_EVEN:",
      number.quantize(Decimal("0.0")))

# Округлення вверх при нічиї (ROUND_HALF_UP)
print("Округлення вгору ROUND_HALF_UP:", number.quantize(
    Decimal("0.0"), rounding=decimal.ROUND_HALF_UP))

# Округлення вниз (ROUND_FLOOR)
print("Округлення вниз ROUND_FLOOR:", number.quantize(
    Decimal("0.0"), rounding=decimal.ROUND_FLOOR))

# Округлення вверх (ROUND_CEILING)
print("Округлення вгору ROUND_CEILING:", number.quantize(
    Decimal("0.0"), rounding=decimal.ROUND_CEILING))

# Округлення до трьох десяткових знаків за замовчуванням
print("Округлення до трьох десяткових знаків:",
      Decimal("3.14159").quantize(Decimal("0.000")))
