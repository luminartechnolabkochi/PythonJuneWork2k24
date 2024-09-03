# List =[]
# Tuple =()
# set=set()
# Ditionary

# dict={key:value}
# student ={"name":"sukumar","course":"fullstack",'course':"Datascience"}
# print(student)

# <class dict> :collection of elements as a key:value pair 

# print(student["name"])

# print(student.keys())     #retuns the keys in the dictionary
# student["name"]="hari" #
# student['place']="chennai"       #overwrites the value if the key is present else add as a new pair



# new=student.items()
# print(new)   #dict_items([('name', 'hari'), ('course', 'fullstack'), ('place', 'chennai')])



student ={"name":"sukumar",'course':"Datascience","place":"chennai"}


# for i in student:

#       print(f"{i} = {student[i]}")


# update the course as fullstack in students in  iteration 
# for i in student:
      
#       if i == "course":
            
#             student[i]="fullstack"

# print(student)

# delete a key "place" if it present in the dict using iteration

# for key,value in student.items:

#     if key=="place":

#         del student[key]

# print(student)




# student.pop("place") # remove the key : value from the dictionary if its present
