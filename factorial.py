n=int(input("Enter a positive no:"))
p=1
if(n<0):
    print('Sorry, this program is not made for negative numbers')
elif(n==0):
    print("It seems like you entered zero")
else:
    for i in range(1,n+1):
        p=p*n
    print('The factorial of your number is :-',p)
    
   
