n = int(input("Enter Number Of Dictionary Items : "))
d = {}
for i in range(n):
    print("Enter Dict Key(RollNumber) ",i+1)
    k = int(input())
    print("Enter Dict Value(Name) ", i+1)
    d[k] = input()
print(d)
da = sorted(d.items())
print("------------------------\nA S C E N D I N G  O R D E R\n------------------------\n",da)
da.reverse()
print("------------------------\nD E S C E N D I N G  O R D E R\n------------------------\n",da)