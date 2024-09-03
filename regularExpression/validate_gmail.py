# starting with aplhanumeric
# [a-zA-Z0-9._]
# @gmail.com


from re import fullmatch


gamail_id=input("enter gmail id")


pattern="\\w[\\w\\._]*@gmail.com"

matcher=fullmatch(pattern,gamail_id)

print("invalid" if matcher==None else "valid")

# + match one or more
# ? optional
# * zero or more

# pattern=""

