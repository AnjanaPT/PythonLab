class rectangle:
    def __init__(self,l,b):
        self.__l=l
        self.__b=b
        self.a=0
    def displayR(self):
        print("--------------------------------------------\nLength %9s" %(":"),"%2s" %(self.__l))
        print("Breadth %8s" %(":"),"%2s" %(self.__b))
    def __lt__(self,r):
        self.a = self.__l * self.__b
        r.a = r.__l * r.__b
        print("--------------------------------------------\nRECTANGLE 1")
        rectangle.displayR(self)
        print("Area %11s" %(":"),"%2s" %(self.a))
        print("--------------------------------------------\nRECTANGLE 2")
        rectangle.displayR(r)
        print("Area %11s" % (":"), "%2s" % (r.a),"\n--------------------------------------------")
        if(self.a < r.a):
            print("Area Of Triangle 1 ( %f " %(self.a),") Is Less Than The Area Of Triangle 2 ( %f " %(r.a),")")
        elif (self.a == r.a):
            print("Area Of Triangle 1 ( %f " % (self.a), ") Is Equal To The Area Of Triangle 2 ( %f " %(r.a),")")
        else:
            print("Area Of Triangle 1 ( %f " %(self.a),") Is Greater Than The Area Of Triangle 2 ( %f " %(r.a),")")
l1=float(input("--------------------------------------------\nEnter Length Of The Rectangle 1         : "))
b1=float(input("Enter The Breadth Of The Rectangle 1    : "))
r1=rectangle(l1,b1);
l2=float(input("--------------------------------------------\nEnter Length Of The Rectangle 2         : "))
b2=float(input("Enter The Breadth Of The Rectangle 2    : "))
r2=rectangle(l2,b2);
r1 < r2