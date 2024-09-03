num=int(input("enter number"))#153

original=num

total=0

digit_count=len(str(num))

while(num!=0):#1634

    digit=num%10

    exponent=digit**digit_count

    total=total+exponent

    num=num//10#0
    
print("Armstrong number" if original==total else "not Armstrong")
