# wap to find the smallest numer

# number= [3,2,5,7,1,9,10,4]


# smallest_num = number[0]

# for i in number:

#     if  i < smallest_num:

#         smallest_num = i

# print(f"the smallest number in the list is {smallest_num}")

#numbers= [1,2,[3,(100,200,300),4],5,6] >>> [1,2,[3,4,(100,150,200,300)],5,6]

number= [5,7,9,10,4,3]


smallest_num = number[-1]     #1

secon_smallest=number[0]      #2

for i in number:
     
    if i < secon_smallest and i < smallest_num:  # 3< 2      3<1

        secon_smallest=smallest_num      

        smallest_num=i                 

    elif i<secon_smallest and i > smallest_num:   # 3<2

        secon_smallest=i   #2

print(secon_smallest)


# 0 invalid

#numbers= [1,2,[3,(100,200,300),4],5,6] >>> [1,2,[3,4,(100,150,200,300)],5,6]

# numbers= [1,2,[3,(100,200,300),4],5,6]

# new=numbers[2]

# ele_four=new.pop()

# new.insert(1,ele_four)   #[3, 4, (100, 200, 300)]
# print(new)

# numbers[2]=new
# print(numbers)

# new1=numbers[2][2]
# l=list(new1)
# l.insert(1,150)
# l1=tuple(l)
# numbers[2][2]=l1
# print(numbers)        #[1, 2, [3, 4, (100, 150, 200, 300)], 5, 6]


