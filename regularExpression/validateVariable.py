# first letter alphabet
# followed by any number of alphabets and numbers


from re import fullmatch

variable_name=input("enter variable name>")#num1

pattern="[a-zA-Z][a-zA-Z0-9_]*"

matcher=fullmatch(pattern,variable_name)


print("invalid" if matcher==None else "valid")

