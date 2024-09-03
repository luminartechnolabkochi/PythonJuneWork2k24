
from re import finditer

text="hellopyhtonhellopythonhellopython"


matcher=finditer("python",text) #(start,group)

count=0

for m in matcher:

    print(m.start(),"===",m.group())

    count+=1

print("total count",count)

