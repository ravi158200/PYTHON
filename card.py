pin=1234
for i in range(3):
    p=int(input("Enter your pin:"))
    if p==pin:
        print("correct pin")
        print("Transaction Successful")
        break
    else:
        print("Incorrect Pin")
else:
    print("card Blocked")
