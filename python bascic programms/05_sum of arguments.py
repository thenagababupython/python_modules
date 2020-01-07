from sys import argv
sum=0
args=argv[1:]
for x in args:
    n=int(x)
    print("n",n)
    sum=sum+n
    print(sum)