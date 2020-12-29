s1 = input("Enter The First String : ")
s2 = input("Enter The Second String : ")
s = s2[:2]+s1[2:]+" "+s1[:2]+s2[2:]
print(s)