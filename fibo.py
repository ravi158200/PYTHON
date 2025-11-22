r=int(input("Enter a range"))
a=0
b=1
for i in range(r):
    c=a+b
    print(c)
    a=b
    b=c
