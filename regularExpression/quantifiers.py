
from re import finditer
#91+{1} 5679999
# {} ? * +

text="ab12xyz678#$pqr123cdef"

# c-h or t-z
pattern="([a-z]{3}|[0-9]{3})"

matcher=finditer(pattern,text)

for m in matcher:

    print(m.start(),"===",m.group())
