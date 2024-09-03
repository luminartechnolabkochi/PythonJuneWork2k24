landslide_death_count = [
    {"state": "Kerala", "year": 2018, "deaths": 14},
    {"state": "Uttarakhand", "year": 2018, "deaths": 15},
    {"state": "Himachal Pradesh", "year": 2018, "deaths": 10},
    {"state": "Kerala", "year": 2019, "deaths": 12},
    {"state": "Uttarakhand", "year": 2019, "deaths": 5},
    {"state": "Himachal Pradesh", "year": 2019, "deaths": 4},
    {"state": "Kerala", "year": 2020, "deaths": 66},  # Pettimudi landslide on August 6
    {"state": "Uttarakhand", "year": 2020, "deaths":6},
    {"state": "Himachal Pradesh", "year": 2020, "deaths":8},
    {"state": "Kerala", "year": 2021, "deaths": 35},
    {"state": "Himachal Pradesh", "year": 2021, "deaths": 37},
    {"state": "Maharashtra", "year": 2021, "deaths": 117},
    {"state": "Uttarakhand", "year": 2021, "deaths": 4},
    {"state": "Karnataka", "year": 2021, "deaths": 0},  # No specific death count mentioned
    {"state": "Kerala", "year": 2022, "deaths": 3},
    {"state": "Uttarakhand", "year": 2022, "deaths":1},
    {"state": "Himachal Pradesh", "year": 2022, "deaths": 2}
]


f=open("C:\\Users\\Luminar\\Desktop\\PythonJuneWorks\\FileOperations\\land_slides.txt","w")

for data in landslide_death_count:

    f.write(data.get("state")+" "+str(data.get("year"))+" "+str(data.get("deaths"))+"\n")


