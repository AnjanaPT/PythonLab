a=float(input("Enter first number : "))
b=float(input("Enter second number : "))
print("SWAPPING WITHOUT TEMPORARY VARIABLE\n-------------------------")
print("BEFORE SWAPPING\n-------------------------\na :",a,"  b :",b)
a,b=b,a
'''a=a+b
b=a-b
a=a-b'''
'''a=a^b
b=a^b
a=a^b'''
print("\nAFTER SWAPPING\n-------------------------\na :",a,"  b :",b)