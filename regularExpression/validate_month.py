# validate_month


# 01
# 02
# 09
# 10
# 12

from re import fullmatch
month="2"

pattern="(0?[1-9]|1[0-2])"

matcher=fullmatch(pattern,month)

print("invalid" if matcher==None else "valid")

# date 01 1,10,11,12,19,31

