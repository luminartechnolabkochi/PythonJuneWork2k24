
from json import load

f=open("C:\\Users\\Luminar\\Desktop\\PythonJuneWorks\\jsonWorks\\data.json")

products=load(f)

for p in products:

    print(p.get("title"))


