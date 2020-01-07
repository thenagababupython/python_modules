def arm(n):
    temp = 0
    l = len(str(n))
    for i in str(n):
        temp = temp + int(i) ** l
        if temp == n:
            return "armstrong"
    else:
        return "not arm strong"


print(arm(153))
