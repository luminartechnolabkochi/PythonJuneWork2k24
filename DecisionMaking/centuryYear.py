# read a year from user and 
# print century year if year ends with two zeros 
# else print non century year 


year = int(input("enter year"))

if year%100 == 0:

    print(f"{year}century year")

else:

    print(f"{year}non century year")


