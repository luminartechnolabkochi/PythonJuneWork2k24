
from json import load

f=open("C:\\Users\\Luminar\\Desktop\\PythonJuneWorks\\jsonWorks\\products.json",encoding="UTF-8")


items=load(f)

# items=[{},{},,,,,{}]

# arr=[10,20,30]

# print(len(items))

# print(items.get("title"))


item_titles=[i.get("title") for i in items]

# print(item_titles)

jwelery_products=[i.get("title") for i in items if i.get("category")=="jewelery" ]

# print(jwelery_products)


price_filter=[i.get("id") for i in items if  i.get("price")>=100 and i.get("price")<=150]


print(price_filter)

# product with most number of ratings


def get_rating_count(dic):

    return dic.get("rating").get("count")



top_selling_product=max(items,key=get_rating_count)

print(top_selling_product)




