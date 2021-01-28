l = (input("Enter A String : ").lower()).split()
d = {}
for i in l:
    if i in d:
        m = d[i]
        d[i] =m+1
    else:
        d[i] = 1
print("%20s : %5s "%("WORD","OCCURRENCE\n        ---------------------------------"))
for i in d:
    print("%20s : %5d "%(i,d[i]))
