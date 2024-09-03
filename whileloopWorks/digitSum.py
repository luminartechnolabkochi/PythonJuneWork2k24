#read a number print sum of digit

# input=543
# output=12

num=int(input("enter number"))

total=0
while(num!=0):

    digit=num%10

    total=total+digit

    num=num//10

print(total)

# sum of cube of each digit 
# 543
# 5^3+4^3+3^3