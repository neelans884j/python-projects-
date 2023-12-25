p=("What is your Name")
i=0
l=(p[4])
o=(p[3])
while(i<=16):
    j=i+l
    m=i+o
    if(j==4 or m==7):
        print("$",end=" ")
        if(i==12):
            print("4",end=" ")
    print(p[i],end=" ")
    i=i+1
