def pattern(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(i*j,end=' ')
        print()
l = int(input("Enter The No Of Levels : "))
pattern(l)