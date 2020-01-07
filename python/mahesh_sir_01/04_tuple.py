w = input("enter string:")
s = {'a', 'e', 'i', 'o', 'u'}
d = s.intersection(w)
print(d)


def sum(*n):
    total = 0
    for n1 in n:
        total = total + n1
    print(total)


sum()
sum(10)
sum(10, 20)
sum(10, 20, 30)
