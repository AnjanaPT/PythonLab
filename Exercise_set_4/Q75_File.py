f1=open('Q75_File.txt','r')
fo=open('Q75_Odd.txt','w')
fe=open('Q75_Even.txt','w')
for i in map(int,f1.readline().split()):
    if i%2==0:
        fe.write(str(i)+" ")
    else:
        fo.write(str(i)+" ")
