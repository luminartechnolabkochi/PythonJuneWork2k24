

class Employee:

    eid:int

    name:str

    age:int

    gender:str

    department:str

    # initializing instance variables=>constructor
    # constructor unique name
    # java=>classname()
    # javascript => constructor()
    # python=>__init__()
    # 


    def __init__(self,id,name,age,gender,dept):

        self.eid=id

        self.name=name

        self.age=age

        self.gender=gender

        self.department=dept


    def display_employee(self):

        print(self.name,self.id,self.department)





