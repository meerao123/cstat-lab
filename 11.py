#Count the number of words, sentences, uppercase letters, lowercase letters, and special symbols in a text file.
file=open("file.txt","r")
text=file.read()
file.close()
words=len(text.split())
sentances=0
special=0
upper=0
lower=0

for ch in text:
    if ch in '.!?':
        sentances+=1
for ch in text:
    if ch.islower():
        lower+=1
    elif ch.isupper():
        upper+=1
    elif not ch.isalnum() and not ch.isspace():
        special+=1
print("words ",words)
print("Sentances",sentances)
print("Special", special)
print("lower", lower)
print("upper",upper)