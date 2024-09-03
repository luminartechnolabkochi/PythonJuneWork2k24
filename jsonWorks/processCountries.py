
from  json import load

f=open("C:\\Users\\Luminar\\Desktop\\PythonJuneWorks\\jsonWorks\\countries.json",encoding="UTF-8")


data=load(f)


# print(len(data))

def fetch_country_by_name(name):

    return [c for c in data if c.get("name")==name][0]


country_data=fetch_country_by_name("Benin")

if "regionalBlocs" in country_data:

    bloc_data=country_data.get("regionalBlocs")[0]

    if "otherNames" in bloc_data:

        print(bloc_data.get("otherNames"))

    else:

        print(country_data.get("name"))




def get_area(dic):

    if "area" in dic:

        return dic.get("area")
    else :
        return 0

biggest_country_by_area=max(data,key=get_area)

# print(biggest_country_by_area.get("name"))

for c in data:

    for l in c.get("languages"):

        if l.get("name")=="English":

            print(c.get("name"))




all_regions={c.get("region") for c in data }

print(all_regions)


region_summary={}#Asia:

for c in data:

    region_name=c.get("region")

    if region_name in region_summary:

        region_summary[region_name]+=c.get("area",0)

    else:

        region_summary[region_name]=c.get("area",0)
    

value_key=[(v,k) for k,v in region_summary.items()]

print(max(value_key))


# regular expression
# (kl)-digit{1,2}-alphabet{1,2}-digit{4}

# digit{10}
# pancard number  DTZPS6463j
# p


