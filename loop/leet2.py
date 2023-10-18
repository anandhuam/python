v=int(input("Enter the number :"))
a=v
reverse=0
while(v>0):
    num=v%10
    reverse=reverse*10+num
    v=v//10
if(a==reverse):
    
    print(a,"is palindrome")
else:
       print(a,"is not palindrome")
    
  