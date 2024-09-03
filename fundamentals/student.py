
# write a program to read student name and 3 marks mark1,mark2,mark3
# and print total mark and average mark

# SET student_name

student_name=input("enter student name")

# SET mark1
mark1=int(input("enter mark1"))#"45"

# SET mark2
mark2=int(input("enter mark2"))#"40"

# SET mark3
mark3=int(input("enter mark3"))#"40"

# CALCULATE total
total=mark1+mark2+mark3
# CALCULATE avg
avg=total/3
# DISPLAY student_name total avg
print(f"student {student_name} total mark ={total} avg={avg}")

