n1 = int(input("Enter First Number : "))
n2 = int(input("Enter Second Number : "))
if(n1==0 and n2==0):
    print("Gcd Is : ",n1)
elif(n1==0 and n2>0):
    print("Gcd Is : ",n2)
elif(n2==0 and n1>0):
    print("Gcd Is : ",n1)
else:
    while(n1!=n2):
        if(n1>n2):
          n1 = n1-n2
        else:
          n2 = n2-n1
    print("Gcd Is : ",n1)