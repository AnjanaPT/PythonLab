d1 , d2 , d3 = {} , {} , {}
n1 = int(input("Enter The Number Of Items In Dictionary 1 : "))
for i in range(n1):
    print("\nEnter Key(Name) ", i + 1," : ",end=' ')
    k = input()
    print("Enter The Value(No) For Key ", k," : ",end=' ')
    d3[k]=d1[k] = int(input())
n2 = int(input("\nEnter The Number Of Items In Dictionary 2 : "))
for i in range(n2):
    print("\nEnter Key(Name) ", i + 1," : ",end=' ')
    k = input()
    print("Enter The Value(No) For Key ", k," : ",end=' ')
    d2[k] = int(input())
for k in d2:
    if k in d3:
        d3[k] += d2[k]
    else:
        d3[k] = d2[k]
print("\nDICTIONARY 1 :      ",d1,"\nDICTIONARY 2 :      ",d2,"\nMERGED DICTIONARY : ",d3)