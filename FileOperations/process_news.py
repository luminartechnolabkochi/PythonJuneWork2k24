
f=open("C:\\Users\\Luminar\\Desktop\\PythonJuneWorks\\FileOperations\\news.txt","r")




word_list=[w for line in f for w in line.rstrip("\n").split(" ") if w !=""]


wc={w:word_list.count(w) for w in word_list}

print(wc)


srt=sorted(wc,key=lambda key:wc.get(key),reverse=True)
print(srt)