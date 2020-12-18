s = input("Enter The String : ")
p = int(input("Enter The Position From Which The Element To Be Deleted : "))
s=s[:p]+s[p+1:]
print(s) 