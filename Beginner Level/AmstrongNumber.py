x=int(input("enter a number"))
temp=x
sum=0
while (temp>0):    
    a=temp%10
    sum=sum+a**3
    temp=temp//10
if (sum==x):
    print(x,"amstrong")
else:
    print(x,"not amstrong")
