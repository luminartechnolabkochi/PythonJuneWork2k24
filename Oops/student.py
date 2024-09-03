

class Student:

    name:str

    id:int

    gender:str

    age:int

    course:str

    contact:str

    addres:str

    def set_student(self,id,name,gender,age,course,contact,address):

        self.id=id

        self.name=name

        self.gender=gender

        self.age=age

        self.course=course

        self.contact=contact

        self.addres=address

    def display_student(self):

        print(self.id,self.name)

# creating objects


student_instance=Student()

student_instance.set_student(100,"hari","male",24,"django",23456789,"address line 1")

student_instance.display_student()