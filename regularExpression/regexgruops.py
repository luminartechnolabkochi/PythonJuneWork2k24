
from re import finditer

text="abc123 @K#7LMdef!@&"


# pattern="[abf]" #chk for either a b or f

# pattern="[a-k]"#chk for alphabets from a to k

# pattern="[a-z]"#chk for all lowercase alphabets

# pattern="[A-Z]" #chk for all uppercase alphabets

# pattern="[a-zA-Z]"#matching all alphabets

# pattern="[0-9]" #chk for digits

# pattern="[a-zA-Z0-9]"# chk for all alphanumeric characters

# pattern="[^0-9]"

# pattern="[^a-zA-Z0-9\s]"

# pattern="[\s]" #chk for space

pattern="[a-zA-Z0-9\s]"

matcher=finditer(pattern,text)

for m in matcher:
    
    print(m.start(),"==",m.group())




