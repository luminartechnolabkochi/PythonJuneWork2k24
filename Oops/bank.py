class Bank:
    
    def create_account(self,acno,ac_type):

        self.bank_name="SBT"

        self.__balance=2000

        self.acno=acno

        

        self.ac_type=ac_type

    def deposit(self,amount):

        self.__balance+=amount

        print(f"your {self.bank_name}Acc with {self.acno} has benn credited with amount{amount} aval bal{self.__balance}")

    def withdraw(self,amount):

        if amount>self.__balance:#5000>2000
            print("transaction failed insufficient balance")

        else:

            self.__balance-=amount

            print(f"your {self.bank_name}Acc with {self.acno} has benn debited with amount{amount} aval bal{self.__balance}")

    def get_balance(self):

        print(f"avl bal={self.__balance}")


user_account=Bank()

user_account.create_account(10000,"savings")

user_account.withdraw(1000)

user_account.deposit(5000)


#object.attribute


vishnu_account=Bank()
vishnu_account.create_account(3000,"current")
vishnu_account.deposit(5000)

vishnu_account.balance+=20000

# error handling
# try
# except
# finally

# OOPS
# class object
# class (blueprint,design pattern,template)

# class ClasName:

#     # attributes
#     # methods

# self,super()
# reference=ClassName()
# attributes initalize __int__()
# object string representation __str__()
# inheritance
    #signle
    #multiple
    # multilevel
# polymorphism
    #methodoverloading(*args,**kwargs)
    # method overriding()

# abstraction
    #ABC,@abstractmethod

#__attri
