s = input(" Enter A String : ")
r = s[0]
s1 = r+s[1:].replace(r,"$")
print("",s,"\n Replacing Each '",r,"'With '$' Except The First One\n",s1)