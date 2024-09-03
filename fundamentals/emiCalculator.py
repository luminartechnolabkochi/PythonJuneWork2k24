# EMI calculator program

# p=>loan amount
#r=> interest rate (p.a)=> p.m
#t=>tenure(years)=>months

# SET loan_amount
loan_amount=200000
#SET interest_rate
interest_rate=9
#SET tenure
tenure=10
# convert yearly interest rate to montly interest rate

r=interest_rate/12/100

print(r)

n=tenure*12

# # EMI=p*r*(1+r)**n/(1+r)**n-1

one_plus_r=(1+r)**n

EMI=(loan_amount*r*one_plus_r)/(one_plus_r-1)

# TotalInterestPayable

total_payable_amount=EMI*n

print(f"MONTHLY EMI={EMI}")


print(f"Total Payable Amount={total_payable_amount}")


total_interst_payable=total_payable_amount-loan_amount

print(f"Total interest  payable amount={total_interst_payable}")

