text="ABACDDBB"

word_count={}#A:1,B:1,

for char in text:#char=A

    if char in word_count:

        print(char,"first recursive character")

        break
    
    else:

        word_count[char]=1
