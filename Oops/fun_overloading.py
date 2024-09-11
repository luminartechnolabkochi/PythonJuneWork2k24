

number=10.5

print(isinstance(number,(int,float)))


# *args (argumaents tuple)
# **kwargs(keyword arguments dictionary)

def get_person(**kwargs):#args=("hari","tvm","kakkanad")

    print(kwargs.get("name"))
    print(kwargs.get("w_place"))

    
get_person(name="hari",w_place="tvm",n_place="kakkanad")





def flat_list(*args):#

    flat=[]

    for arg in args:

        if isinstance(arg,list):

            flat.extend(flat_list(*arg))
        
        else:

            flat.append(arg)
    
    return flat

print(flat_list((10,20,[100,200],[1000,[2000,3000]])))





