a = float(input("Enter First Number  : "))
b = float(input("Enter Second Number : "))
c = float(input("Enter Third Number  : "))
if a>b and a>c:
    print(a," is the largest among the given numbers")
elif b>c:
    print(b," is the largest among the given numbers")
elif c>b:
    print(c," is the largest among the given numbers")
else:
    print("All three given numbers are equal")