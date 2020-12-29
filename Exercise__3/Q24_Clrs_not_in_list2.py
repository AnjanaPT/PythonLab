c1 = input("Enter The First List Of Colors : ").split()
c2 = input("Enter The Second List Of Colors : ").split()
print(c1)
print(c2)
c1 = [i for i in c1 if i not in c2]
print(c1)