

source_word="REGULATE"

target_word="RULE"

word_count={}#R:1,E:2

for ch in source_word:

    if ch in word_count:

        word_count[ch]+=1
    
    else:

        word_count[ch]=1

is_kangroo_word=True

for ch in target_word:

    if ch in word_count and word_count.get(ch)>0:

        word_count[ch]-=1

    else:

        is_kangroo_word=False

        break

print(is_kangroo_word)





