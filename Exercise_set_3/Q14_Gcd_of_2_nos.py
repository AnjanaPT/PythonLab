n1 = a = int(input("Enter First Number : "))
n2 = b =  int(input("Enter Second Number : "))
while n2 > 0:
    r = n1 % n2
    n1 = n2
    n2 = r
print("Gcd (",a,",",b,") Is : ",n1)