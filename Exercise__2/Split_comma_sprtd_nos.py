n = input("Enter a sequence of comma separated numbers : ")
l = list(map(float,n.split(',')))
t = tuple(l);
print("\nThe List Is : ",l,"\nThe Tuple Is :",t)