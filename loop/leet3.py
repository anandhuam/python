list=["add","adarsh","admin"]
if not list:
    prefix=""
else:
    list.sort()
    x,y=list[0],list[-1]
    prefix=""
    for i in range(len(x)):
        if i<len(y) and x[i]==y[i]:
            prefix +=x[i]
        else:
            break
        print(prefix)    