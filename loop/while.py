choice='A'
list=["game","movie","market"]
while choice=='A' :
    print('''
 1) display  
 2) delete 
 3) add  
 4) quit
         ''' )
    
    option=input("Enter your choice:")
    
    if option=='1':
        print (list)
        
    elif option=='2':
        a=input("enter the item you want to delete:")
        list.remove(a)
        
    elif option=='3':
        b=input("enter the item to add:")
    
        list.append(b)
        
    elif option=='4':
        exit()
    else:
        print('enter a valid choice') 
         
    

    