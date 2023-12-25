import time 
tl=1
alert=("\a\a")
beep=str(input("Enter the passcode ="))
if(beep=="password"):
    print("well done")
else:
      print(" Warning!\nA stranger is detected")
while True:
    while (tl<=20):
        print(alert)
    
    print()
       

