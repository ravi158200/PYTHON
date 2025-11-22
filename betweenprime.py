s=int(input("Enter starting Number:"))
e=int(input("Enter ending Number:"))
for x in range(s,e):
    for i in range(2,x):
        if(x%i==0):
            break
        else:
            print(x,end="  ")
        
