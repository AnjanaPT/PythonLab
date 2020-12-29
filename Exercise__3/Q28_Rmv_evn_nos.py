s = input("Enter The Numbers : ")
l = list(map(int,s.split()))
l2 = [i for i in l if i%2!=0]
print("List After Removing Even Numbers : ",l2)
