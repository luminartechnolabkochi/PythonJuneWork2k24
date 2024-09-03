# wap to find the secondlargest number in list

number= [12,2,5,7,1,11,10,4]

largest_num = number[0]

second_largest_num = 0
for  i in number:
    print(i)
    if  i >second_largest_num and i > largest_num:

        second_largest_num = largest_num
        print(second_largest_num)
        largest_num = i
        print(largest_num)

    elif i > second_largest_num and i < largest_num:

        second_largest_num = i

print(f" second largest num is {second_largest_num}")



# list 

# number =[1,2,3,4] insertion order preserved  index ,Duplicates allowed ,number=[],mutable


# wap to find the sum of odd numbers  in the list

# wap to find the count of even and odd numers in th list


numbers= (1,2,3,4)  # Tuple   define by (), 

print(numbers[1])   # indesxx positioning , duplicates allow ,immutable,index(),count()



