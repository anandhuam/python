choice='x'
bank=[]
new_customer={}
accont_no=0
while choice=='x' :
     print('''
1)add
2)display
3)add balance
4)withdraw
5)quit
           ''')
     option=int(input("Enter your choice:-"))
     if option==1:
         name=input("Enter customer name:")
         age=input("Enter customer age:")
         contact=input("Enter customer contact no:")
         accont=input("Enter customer account no:")
         new_customer["name"]=name
         new_customer["age"]=age
         new_customer["contact no:"]=contact
         new_customer["accont no:"]=accont_no+1
         new_customer["balance:"]=0
         bank.append(new_customer.copy())

     elif option==2:
          print(bank)
          
     elif option==3:
          accont=input("Enter customer account no:")
          a=input("Enter the amount to add")
          print(new_customer[balance]+a)
          
          
          
          
          
     elif option==4:
          print()
          
          
     elif option==5:
          exit()