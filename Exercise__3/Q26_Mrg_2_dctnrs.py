d1 = {}
d2 = {}
d3 = {}
n1 = int(input("Enter The Number Of Items In Dictionary 1 : "))
for i in range(n1):
    print("\nEnter Key ", i + 1," : ",end=' ')
    k = input()
    print("Enter The Value For Key ", k," : ",end=' ')
    d1[k] = int(input())
    d3[k] = d1[k]
n2 = int(input("\nEnter The Number Of Items In Dictionary 2 : "))
for i in range(n2):
    print("\nEnter Key ", i + 1," : ",end=' ')
    k = input()
    print("Enter The Value For Key ", k," : ",end=' ')
    d2[k] = int(input())
    if k in d3:
        d3[k] += d2[k]
    else:
        d3[k] = d2[k]
print("\nDICTIONARY 1 :      ",d1,"\nDICTIONARY 2 :      ",d2,"\nMERGED DICTIONARY : ",d3)