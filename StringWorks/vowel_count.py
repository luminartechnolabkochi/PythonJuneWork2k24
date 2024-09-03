text="ahello"

vowels="aeiou"

v_count=0

c_count=0

for ch in text:

    if vowels.count(ch)!=0:

        v_count+=1
    else:

        c_count+=1
    

print(v_count)

print(c_count)


# logic2

# for ch in vowels:

#     v_count+=text.count(ch)

# print(v_count)

# 

