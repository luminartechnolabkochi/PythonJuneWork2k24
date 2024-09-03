#tuple
#=======


number=(1,2,3,4)

# duplicate allow

# index position

# insertion order preserved

# immutable   >>>>cannot modify

courses=("python",)

print(type(courses))

# count(),index()  



#set
#===========
# duplicates not allowed

# elements are unordered

# It doesnt have index position

#  mutable 

names={"hello","chennai","hari","kollam"}

new_names={"hp","dell","hello","lenovo"}

# names.update(new_names)  #add elements from any collection to the set

# print(names)

# new_set=names.union(new_names) # return the combined elements from two sets and return as a new set
#new_set=names.intersection(new_names)#return common elements from 2 set objcts as a new set
#new_set=names.difference(new_names)#return elements from set names which is not in set new_names as new set
new_set=names.symmetric_difference(new_names)#combine all elemets from 2 set and remove common elements
print(new_set)
# names.add("Kochi") # to add an element to a set object
# print(names)
# names.clear()  # removes all elements from object ,emplty set remains
# print(names)

# names.pop() # which removes a random element from the set object
# print(names)
# names.discard("hello") # remove an element from the set if its a memeber in the object
# print(names)













