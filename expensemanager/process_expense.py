

f=open("C:\\Users\\Luminar\\Desktop\\PythonJuneWorks\\expensemanager\\data.txt")

expenses=[]

for line in f:

    data=line.rstrip("\n").split(" ")

    expenses.append({"date":data[0],"category":data[1],"amount":data[2]})



category_summary={}

for exp in expenses:

    cat=exp.get("category")

    amount=int(exp.get("amount"))

    if cat in category_summary:
        category_summary[cat]+=amount
    else:
        category_summary[cat]=amount

print(category_summary)



class Person:

    def __init__(self,age,name) :

        self.name=name

        self.age=age

    @property
    def get_age(self):

        return self.age
    
    @property
    def get_name(self):

        return self.name
    
person_instance=Person(32,"hari")

print(person_instance.get_age)
    

