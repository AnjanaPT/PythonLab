n = int(input("Enter Number Of Dictionary Items : "))
d , dkd , dka , dva , dvd= {},{},{},{},{}
for i in range(n):
    print("Enter Dict Key(RollNumber) ",i+1)
    k = int(input())
    print("Enter Dict Value(Name) ", i+1)
    d[k] = input()
print(d)
dka = dict(sorted(d.items()))
dkd = dict(sorted(d.items(),reverse=True))
dv = sorted(d.values())
for i in dv:
    dva[next((key for key,value in d.items() if value==i),None)]=i
for i in dv[::-1]:
    dvd[next((key for key,value in d.items() if value==i),None)]=i
print("------------------------------------------\nA S C E N D I N G  O R D E R\n------------------------------------------")
print("Based On Keys   : ",dka,"\nBased On Values : ",dva)
print("------------------------------------------\nD E S C E N D I N G  O R D E R\n------------------------------------------")
print("Based On Keys   : ",dkd,"\nBased On Values : ",dvd)
