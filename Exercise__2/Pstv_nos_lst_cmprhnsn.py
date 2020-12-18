n = int(input("Enter the number of integers : "))
l = []
for i in range (n):
    print("Enter Number ",i+1)
    l.append(float(input()))
lpn = [i for i in l if i>0]
print("Given Integers                                 : ",l)
print("Positive Integers In The Given Set Of Integers : ",lpn)