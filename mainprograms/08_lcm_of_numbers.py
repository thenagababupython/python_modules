n1 = int(input("enter first number:"))
n2 = int(input("enter second number:"))

if n1 > n2:
    min1 = n1
else:
    min1 = n2
while (True):
    if min1 % n1 == 0 and min1 % n2 == 0:
        print("lcm of two num:", min1)
        break
    min1 = min1 + 1
