fst = input("Enter The First Set Of Integers : ")
scnd = input("Enter The Second Set Of Integers : ")
l1 = list(map(int,fst.split()))
l2 = list(map(int,scnd.split()))
print("---------------------\nL E N G T H\n---------------------")
if len(l1)==len(l2):
    print("Both Of Given Lists Have Same Length.\nLength Both Lists Is : ",len(l1))
else:
    print("Different Lengths\nLength Of List 1 Is : ",len(l1),"\nLength Of List 2 Is : ",len(l2))
print("---------------------\nS U M\n---------------------")
s1 = s2 = 0
for i in l1:
    s1 += i
for i in l2:
    s2 += i
if s1==s2:
    print("Both Of Given Lists Sums To Same Value.\nSum Is : ",s1)
else:
    print("Different Sums\nSum Of Values Of List1 Is : ",s1,"\nSum Of Values Of Lists2 Is : ",s2)
print("---------------------\nD U P L I C A T I O N\n---------------------")
list = [i for i in l1 if i in l2]
if(len(list)>0):
    print("Values Appearing In Both Lists Are : ", list)
else:
    print("No Value Is Appearing Commonly In Both Lists")