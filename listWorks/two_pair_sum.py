

arr=[2,3,4,5]


result=6

# (2,4)


# List

numbers= [1,2,[3,[100,200,300],4],5,6]

print(numbers[2])   #[3, [100, 200, 300], 4]
print(numbers[2][1]) #[100, 200, 300]

#  class  list

    #       def append()   add element to the end of the list
    #       def insert()   add element to the specific position
    #       def count()    
    #       def pop()     remove last element and return the element
    #       def remove()   

num=[1,2,2,3,4]

# print(num.pop())   #removes the last element and return it

# print(num.pop(2))  #removes the item in index 2 and return the value 

# list.remove(element)

# num.remove(2)    # removes the specific element in the list in the first occurence

# print(num)   #[1, 2, 3, 4]

num.extend([5,6,7,8])   # add a collection of elements to a list
print(num)


