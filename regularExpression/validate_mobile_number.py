# country code *

# 10 digit 

# number starting with 6,7,8,9


from re import fullmatch

mobile_number=input("enter mobile number")


pattern="(91)\\s?[6-9]\\d{9}"


matcher=fullmatch(pattern,mobile_number)

print("invalid" if matcher==None else "valid")


