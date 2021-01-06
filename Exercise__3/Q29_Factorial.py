def fact(n):
    f = 1
    for i in range(1,n+1):
        f *= i
    return(f)
no = int(input("Enter An Integer : "))
print("Factorial : ",fact(no))