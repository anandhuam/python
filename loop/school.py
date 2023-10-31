choice='x'
school=[]
student={}
while choice=='x':
    print('''
 1) Add
 2) Display 
 3) Add fees and balance
 4) Quit
         ''' )
    option=int(input("Enter your choice:-"))
    
    if option==1:
        name=input("Enter student name:")
        standard=input("Enter your standard:")
        age=input("Enter your age:")
        student["name"]=name
        student["standard"]=standard
        student["age"]=age
        school.append(student.copy())
         
    elif option=='2':
        print(student)
   
    
        
    
