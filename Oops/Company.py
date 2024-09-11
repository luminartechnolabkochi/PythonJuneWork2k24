

class Person:

    def __init__(self,name,age,gender):

        self.name=name

        self.age=age

        self.gender=gender

    def display(self):

        print(self.name,self.age,self.gender)

    def __str__(self):

        return self.name


class Employee(Person):

    def __init__(self,name,age,gender,eid,department,salary):

        super().__init__(name,age,gender)

        self.eid=eid

        self.department=department

        self.salary=salary

    def display(self):

        super().display()

        print(self.eid,self.department,self.salary)

emp_instance=Employee("vipin",34,"male","eo1","hr",120000)

emp_instance.display()



# constructor
# 
# __init__()
# 
# __str__
# inheritance
# signgle
# ṃultilevl
# multiple

# polymorphisam
# many forms
# 1)method overloading(same method name,diffenet number of arguments) supportX
#2)method overriding

