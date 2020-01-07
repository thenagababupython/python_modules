# 1, 2, 1, 3, 2, 5, 3, 7, 5, 11, 8, 13, 13, 17, …


def fibonacci(num):
    a = 0
    b = 1
    if num < 0:
        print("wrong input")

    elif num == 0:
        return a
    elif num == 1:
        return b
    else:
        for i in range(2, num):
            c = a + b
            a = b
            b = c
        return b


def prime(num1):
    target = 1000
    count = 0

    for i in range(2, target):
        x = 0
        for j in range(2, i):

            if i % j == 0:
                x = 1
                break
        if x == 0:
            count += 1
        if count == num:
            print(i)
            break


num = int(input("enter the number.."))
if num % 2 == 1:
    fibonacci(int(num / 2) + 1)
else:
    prime(int(num / 2))

