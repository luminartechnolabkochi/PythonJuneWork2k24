# numbers= [1,2,[3,[100,200,300],4],5,6]    #[1,2,[3,[100,200,300,500],4],5,6]

# print(numbers[2])  #[3,[100,200,300],4]

# print(numbers[2][1]) #[100,200,300]

# numbers[2][1].append(500)  #[100,200,300,500]

# print(numbers)      #[1,2,[3,[100,200,300,500],4],5,6]





# wap to swap first and last elements in a list


# num=[1,2,3,4,5,6,7]

# num[-1],num[0]=num[0],num[-1]

# print(num)

# wap to return the odd numbers in another list

# num=[1,2,3,4,5,6,7,8]

# odd_num=[]

# for i in num:

#     if i%2!=0:

#         odd_num.append(i)

# print(odd_num)

# wap to remove the even numbers from the list

# num=[1,2,3,4,5,6,7,8]

# for i in num:

#     if i % 2==0:

#         num.remove(i)

# print(num)

# wap to identify the unique elements

# num=[1,2,2,3,4,5,3,6,4,7]


# for i in num:

#     if num.count(i)==1:

#         print(i)


name = ["t","h","o","m","a","s"]

name.sort()

print(name)   #['a', 'h', 'm', 'o', 's', 't']


#wap to print the list of  numbers in descending order
num=[2,3,6,5,1]

num.sort()   #arrange the integers in ascending order and chars in alphabetical order

num.reverse()

print(num)