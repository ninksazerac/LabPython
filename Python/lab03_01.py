#รู้จักกับ STACK
l=input("Enter Input : ").split(",")
list = []
a=0
for x in l:
    if(x[0]=="A"):
        list.append(x[2:len(x)])#len x=4 count 3,4 only

        print(f"Add = {x[2:len(x)]}"+" and "+f"Size = {len(list)} ")

    elif(x[0]=="P"):#list ={10,20,30,40}
        if(len(list)==0):#[]
            print("-1")
        else:

            b=list.pop()#delete 30,40
            print(f"Pop = {b}"+" and "+f"Index = { len(list) } ")

#"Value in Stack ="
print("Value in Stack = ",end='')
if(len(list)==0):#[]
    print("Empty")
else:
    for i in list:
     print(i+" " ,end='')