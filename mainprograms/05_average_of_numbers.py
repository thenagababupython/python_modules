n = int(input("enter no.of elements:"))
a = []
for i in range(0, n):
    e = int(input("enter elements:"))
    a.append(e)
average = sum(a) / n
print("the average is:", average)
print("the sum  is:", sum(a))
