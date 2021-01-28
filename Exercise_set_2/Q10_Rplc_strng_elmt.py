s = input(" Enter A String : ")
s1 = s[0]+s[1:].replace(s[0],"$")
print(" Replacing Each '",s[0],"'With '$' Except The First One\n Replaced String",s1)