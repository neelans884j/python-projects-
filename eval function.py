x=int(input("Enter your number="))
for i in range(1,11):
    print("your", i ,"number:-","\t",(eval('x+i')))


a=[1,2,3]
a=tuple(a)
a[0]= 2
print(a)
