s = input("Enter A String : ").lower()
l = s.split()
d = {}
for i in l:
    if i in d:
        m = d[i]
        d[i] =m+1
    else:
        d[i] = 1
print("----------------------\nWord (Occurrence)\n----------------------")
for i in d:
    print(i," (",d[i],")")
