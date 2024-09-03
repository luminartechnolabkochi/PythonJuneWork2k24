
# variable name

# first character must be an alphabet => k to m

# second letter must be a number that is / by 3
# followed by any number of alphabets and numbers @

from re import fullmatch

varibale_name=input("enter variable name :")


pattern="[k-m][369][a-zA-Z@]*"


matcher=fullmatch(pattern,varibale_name)

print("invalid" if matcher == None else "valid")


