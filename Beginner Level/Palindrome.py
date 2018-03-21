x=int(input("enter a number"))
temp=x
reverse=0
while x>0:
   remainder=x%10
   reverse=(reverse*10)+remainder
   x=x//10
if reverse==temp:
    print("yes")
else:
    print("no")
