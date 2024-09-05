

class Student:

    name:str

    id:int

    gender:str

    age:int

    course:str

    contact:str

    addres:str

    def __init__(self,id,name,gender,age,course,contact,address):

        self.id=id

        self.name=name

        self.gender=gender

        self.age=age

        self.course=course

        self.contact=contact

        self.addres=address

    def display_student(self):

        print(self.id,self.name)

    def __str__(self):

        return self.name

# creating objects


student_instance=Student(100,"hari","male",24,"django",23456789,"address line 1")


print(student_instance)