n = int(input("Enter The Number Of Colors : "))
cl = []
print("Enter ",n," Colors")
for i in range(n):
    cl.append(input())
print("Given Colors : ",cl,"\nFirst Color  : ",cl[0],"\nLast Color   : ",cl[-1])