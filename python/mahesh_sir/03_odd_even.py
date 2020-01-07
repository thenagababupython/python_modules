"""s = input("entere your some string:")
print("even", s[0::2])
print("even", s[1::2])
"""
s = input("enter your string:")
i = 0
while i < len(s):
    print(s[i], end="")
    i = i + 2
print()
i = 1
while i < len(s):
    print(s[i], end="")
    i = i + 2

