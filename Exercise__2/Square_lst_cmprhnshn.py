n = int(input("Enter the number of integers : "))
l = []
print("Enter ",n," Integers")
for i in range (n):
    l.append(float(input()))
sqr = [i**2 for i in l]
print("Given Integers           : ",l)
print("Square Of Given Integers : ",sqr)