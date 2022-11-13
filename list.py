list=["remya"]
print("list=",list)
def count_letter(word,letter):
    print("word=",word)
    print("letter=",letter)
    print("number of occurences of",letter,"is",end="")
    count=0
    for a in word:
        if(a==letter):
            count=count+1
    return count
x=count_letter("remya","a")
print(x)