



words=["hello","hello","hi","hello"]


word_set=set(words)

for w in word_set:

    print(w,words.count(w))

word_count={}#hello:1

for w in words:

    if w in word_count:

        word_count[w]+=1

    else:
        word_count[w]=1

print(word_count)





