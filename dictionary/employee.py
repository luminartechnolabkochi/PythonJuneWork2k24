employee={
          "name":"hari",
          "dept":"r&d",
          "salary":50000,
          "combo_offer":1000,
          "extra_working_days":3
          }


# print all key value

for k,v in employee.items():

    print(k,v)

# print employee netpay

if "extra_working_days" in employee:

    net_pay=employee.get("salary")+employee.get("combo_offer")*employee.get("extra_working_days")

    print(net_pay)

else:

    net_pay=employee.get("salary")

    print(net_pay)



# fetching value from ditionary using key dict.get(key)

# adding new key value pair dict[key]=value



