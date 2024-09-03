students=[
    {"id":100,"name":"vipin","course":"django","mark":450},
    
    {"id":101,"name":"shibin","course":"django","mark":470},
    
    {"id":103,"name":"jibin","course":"testing","mark":375},
    
    {"id":104,"name":"abin","course":"testing","mark":480},
    
    {"id":105,"name":"dibin","course":"mearn","mark":440},
    
    {"id":106,"name":"vinu","course":"mearn","mark":430},
    
    {"id":107,"name":"tom","course":"asp","mark":460},
]




total=sum([st.get("mark") for st in students])

print(total)


minimum= min([st.get("mark") for st in students ])

print(minimum)









