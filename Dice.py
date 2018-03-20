from random import*
x=input()
roll='y'
while roll=='y':
    x=randint(1,6)
    print(x)
    if x==1 or x==6:
        print("you have another chance")
        roll='y'
    else:
        print("your chance over")
        roll='n'
       
               
