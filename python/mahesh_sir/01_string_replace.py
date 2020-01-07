# s = "Learing Python is Very Easy"
# s1 = s.replace("Easy", "diffcult")
# print(s1)
# ===============================================================================
# s = "abab"
# s1 = s.replace("a", "b")
# print(s, "is avilable at:", id(s))
# print(s1, "is avilable at:", id(s1))
# ======================================================================================
# s = "durga software solutions"
# l = s.split()
# print(l)
# print(type(l))
# for i in l:
#     print(i)
# =========================================================================================

# s = "29-09-2018"
# l = s.split('-')
# for x in l:
#     print(x)
# ========================================================================================
# t=('sunny','bunny','chinny')
# s='-'.join(t)
# print(s)
# ========================================================================================
# s="Learing Python is Very Easy"
# print(s.lower())
# print(s.upper())
# print(s.swapcase())
# print(s.title())
# print(s.capitalize())
# ==========================================================================================

# s = input("enter a string:")
# s1 = input("enter starting srring:")
# s2 = input("enter ending srring:")
# print(s.startswith(s1))
# print(s.endswith(s2))
# ==========================================================================================

# print("python333".isalnum())
# print("python333".isalpha())
# print("python".isalpha())
# print("python".isdigit())
# print("970006070".isdigit())
# print("Python Is Easy".istitle())
# print("Python Is easy".istitle())
# print("Python Is easy".isupper())
# print("PYTHON".isupper())
# print("PYTHON".islower())
# print("python".islower())
# print(" ".isspace())
# ===============================================================================================

# s = input("enter a string:")
# if s.isalnum():
#     print("it is alphanumeric character")
#     if s.isalpha():
#         print("it is alpha character")
#         if s.islower():
#             print("it is lower case")
#         else:
#             print("upper case alphabet character")
#     else:
#         print("it is digit")
# elif s.isspace():
#     print("it is space character")
# else:
#     print("it is special character")
# ============================================================================================
# name = "Naga Babu"
# salary = 50000
# age = 23
# print("{} 's salary is {} and his age is {}".format(name, salary, age))
# print("{0} 's salary is {1} and his age is {2}".format(name, salary, age))
# print("{x} 's salary is {y} and his age is {z}".format(x=name, y=salary, z=age))
# ================================================================================================
# s=input("enter a string:")
# print(s[::-1])  #first method
# print("".join(reversed(s)))  #second method
#
# for i in reversed(s):     #third method
#     print(i,end="")

# ==================================================================================================

# s = input("enter a some string:")
# i = len(s) - 1
# target = ''
# while i >= 0:
#     target = target + s[i]
#     i = i - 1
# print(target)
# ==============================================================================
# import keyword
# print(keyword.kwlist)
#
# =======================================================================================
# reverse string

# s=input("enter some string:")
# print(s[::-1])

# s=input("enter some some string:")
# for i in reversed(s):
#     print(i,end="")

# s = input("eneter some string:")
# i = len(s) - 1
# target = ''
# while i >= 0:
#     target = target + s[i]
#     i = i - 1
#
# print(target)

"""s=input("enter a some string:")
print("".join(reversed(s)))"""

