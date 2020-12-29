n = input("Enter The Numbers : ")
l = list(map(int,n.split()))
l1 = []
for i in l:
    if(i >= 100):
        l1.append("Over")
    else:
        l1.append(i)
print("Given List Of Numbers : ",l,"\nNumbers Greater Than 100 As OVER : ",l1)

