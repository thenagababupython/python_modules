vowels=['a','e','i','o','u']
word=input("enter word:")
foud=[]
for letter in word:
    if letter in vowels:
        if letter not in foud:
            foud.append(letter)
print(foud)