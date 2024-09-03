
from re import fullmatch

f=open("C:\\Users\\Luminar\\Desktop\\PythonJuneWorks\\regularExpression\\domain.txt")


pattern="[\w\W]+\\.com"

for line in f:

    domain=line.rstrip("\n")

    matcher=fullmatch(pattern,domain)

    if matcher !=None: 

        print(domain)