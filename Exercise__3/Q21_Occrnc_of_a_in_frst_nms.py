nm = input("Enter A Set Of Names : ")
l = nm.split(",")
f = []
for i in l:
    f.append((i.split())[0])
print("List Of Names : ",l,"\nList Of First Names : ",f)
c = 0
for i in f:
    for j in i :
        if j in "aA":
            c+=1
print("Occurrence Of 'A' or 'a' In The List Of First Names Is : ",c)