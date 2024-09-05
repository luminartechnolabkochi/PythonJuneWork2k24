

class Mobile:

    name:str

    storage:str

    price:int

    brand:str
#instance variable

    def __init__(self,name,storage,price,brand):
        #instance varibale initialize
        self.name=name

        self.storage=storage

        self.price=price

        self.brand=brand

    def display_details(self):

        print(self.name,self.storage)

    def __str__(self):

        return self.name




mobile_instance=Mobile("nord9r","128",567,"oneplus")



print(mobile_instance)

