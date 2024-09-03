

# kerala vehicle registration number validation

# starting with KL
# two digits
# aplhabets(one or two)
# 4digits 


from re import fullmatch

vehicle_num=input("enter vehicle number  :")

pattern="(KL)(-)?[0-9]{2}(-)?[A-Z]{1,2}(-)?[0-9]{4}"

matcher=fullmatch(pattern,vehicle_num)

print("invalid" if matcher==None else "valid")
