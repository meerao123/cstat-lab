#Count the number of vowels, consonants, words, and question marks in a string.
s=input("enter a string: ")
words=len(s.split())
consonant=0
qn=0
vowels=0

for ch in s :
	if ch.lower() in 'aeiou':
		vowels+=1
	elif ch.isalpha():
		consonant+=1
	elif ch=='?':
		qn+=1
	
print("number of words=",words)
print("number of consonants=",consonant)
print("number of vowels=",vowels)
print("number of question marks=",qn)
