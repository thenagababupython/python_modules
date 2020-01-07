with open("abcd.txt",'w') as f:
    list1=["sunny\n","vinny\n","bunny\n","pinny\n",]
    f.writelines(list1)
    print("list lines written to the successfully")
    f.close()