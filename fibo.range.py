r=int(input("Enter a range:"))
a=0
b=1
print(a)
print(b)
for i in range(r):
    c=a+b
    print(c)
    a=b
    b=c
