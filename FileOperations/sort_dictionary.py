

placements={"testing":45,"python":39,"bigdata":32,"asp":56,"java":60}


srt=sorted(placements,key=lambda key:placements.get(key),reverse=True)

print(srt)