import math
# we will make a calculator in this program
# mainly +,-,*,/,//,**
# float always takes integer and decimal value both
print("welcome to Tech-y Trals calculator❤")
print(" NOTE: \nif there is no value in any of block so kindly enter 0\n")
calc=str(input("what would you have to calculate by this program ="))
a=int(input("Enter the first  and biggest value ="))
b=int(input("Enter the second and next value ="))
c=int(input("Enter the third value ="))
d=int(input("Enter the fourth value ="))
e=int(input("Enter the fifth and smallest value ="))
todh=(b+c+d+e)
sq=(a+b+c+d+e)
if(calc == "add"):
    print(a+todh)
else:
    print()
if(calc == "subtract"):
    print(a-todh)
else:
    print()
if(calc == "multiply"):
    print(a*todh)
else:
    print()
if(calc == "divide"):
    print(a/todh)
else:
    print()
if(calc == "multiply"):
    print(a*todh)
else:
    print()
if(calc == "divide"):
    print(a/todh)
else:
    print()
if(calc == "square"):
    print(a**todh)
else:
    print()
if(calc == "float division"):
    print(a//todh)
else:
    print()    
if(calc == "root "):
    print(math.sqrt(sq))
else:
    print()
if(calc == "divide"):
    print(a/todh)
else:
    print()        
    
