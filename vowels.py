word="hai how are you"
vowels="aeiou"
word=word.lower()
b=[]
for i in word:
    if i in vowels:
      b.append(i)
print(b)