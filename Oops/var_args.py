#inheritance
# polymorphisam
# a)method overloading
# b)method overriding 

# varibale length arguments

# def var_arg_function(num1,num2):

#     print(num1,num2)



# def var_arg_function(num1,num2,num3):

#     print(num1,num2)

# args => tuple()
# variable length parameters
def var_arg_fnction(*args):

    print(args)#tuple


var_arg_fnction(10,20)
var_arg_fnction(10,20,30)




arr=[10,20,30]

points=[1,2,3]


arr.extend(points)

print(arr)