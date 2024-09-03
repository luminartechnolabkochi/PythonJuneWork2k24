
from json import load

f=open("C:\\Users\\Luminar\\Desktop\\PythonJuneWorks\\jsonWorks\\filims.json")


movies=load(f)

for m in movies:

    print(m.get("title"))