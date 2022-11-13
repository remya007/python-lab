def word_counts(str):
    counts=dict()
    words=str.split()
    for word in words:
        if word in counts:
         counts[word]+=1
        else:
            counts[word]=1
    return counts
print(word_counts("the sun rises in the east sun sets in the west"))
