class rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b
        self.a=self.p=0
    def displayR(self):
        print("--------------------------------------------\nLength %9s" %(":"),"%2s" %(self.l))
        print("Breadth %8s" %(":"),"%2s" %(self.b))
    def perimeter(self):
        self.p = 2 * (self.l + self.b)
        rectangle.displayR(self)
        print("Perimeter %6s" %(":"),"%2s" %(self.p),"\n--------------------------------------------")
    def area(self):
        self.a = self.l * self.b
        rectangle.displayR(self)
        print("Area %11s" %(":"),"%2s" %(self.a),"\n--------------------------------------------")
    def __gt__(self,r):
        self.a = self.l * self.b
        r.a = r.l * r.b
        if(self.a > r.a):
            print("Area Of Triangle 1 ( %f " %(self.a),") Is Greater Than The Area Of Triangle 2 ( %f " %(r.a),")")
        elif (self.a < r.a):
            print("Area Of Triangle 1 ( %f " % (self.a), ") Is Less Than The Area Of Triangle 2 ( %f " % (r.a),")")
        else:
            print("Area Of Triangle 1 ( %f " %(self.a),") Is Equal To The Area Of Triangle 2 ( %f " %(r.a),")")
op=''
l1=float(input("--------------------------------------------\nEnter Length Of The Rectangle 1         : "))
b1=float(input("Enter The Breadth Of The Rectangle 1    : "))
r1=rectangle(l1,b1)
l2=float(input("--------------------------------------------\nEnter Length Of The Rectangle 2         : "))
b2=float(input("Enter The Breadth Of The Rectangle 2    : "))
r2=rectangle(l2,b2)
while op != '4':
    print("--------------------------------------------\n1 : Perimeter\n2 : Area\n3 : Compare Area\n4 : EXIT\n--------------------------------------------")
    op=input("Enter Your Option                     : ")
    print("--------------------------------------------")
    if op=='1':
        print("RECTANGLE 1")
        r1.perimeter()
        print("RECTANGLE 2")
        r2.perimeter()
    if op=='2':
        print("RECTANGLE 1")
        r1.area()
        print("RECTANGLE 2")
        r2.area()
    if op=='3':
        r1 > r2
    while op not in "1234":
        op=input("Enter A Valid Option                  : ")


