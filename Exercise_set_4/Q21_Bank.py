class bank:
    def __init__(self,n,no,t):
        self.name=n
        self.ac_no=no
        self.ac_type=t
        self.blnc=0
    def deposit(self,m):
        self.blnc+=m
        print(m, "Rs Successfully Deposited ")
    def balance(self):
        print("Balance : ",self.blnc)
    def withdraw(self,m):
        self.blnc-=m
        print(m, "Rs Successfully Withdrawn ")
    def display(self):
        print("Name : ",self.name,"\nAccount Number : ",self.ac_no,"\nAccount Type : ",self.ac_type)
op=''
n=input("-----------------------------------------\nEnter Your Name : ")
acno=int(input("Enter Your Account Number : "))
actype=input("Enter Your Account Type : ")
b = bank(n, acno, actype)
while op != '5':
    print("-----------------------------------------\n1 : Account Details\n2 : Balance Check\n3 : Deposit\n4 : Withdraw\n5 : EXIT")
    op = input("-----------------------------------------\nEnter Your Option : ")
    print("-----------------------------------------")
    if(op=='1'):b.display()
    if(op=='2'):b.balance()
    if(op=='3'):
        amnt=float(input("Enter The Amount You Want To Deposit : "))
        b.deposit(amnt)
    if (op == '4'):
        b.balance()
        f=''
        if (b.blnc <= 0):
            print("Nothing To Withdraw !!")
        else:
            amnt = float(input("Enter The Amount You Want To Withdraw : "))
            if (b.blnc < amnt):
                f = input("The Amount You Stated Is Less Than Your Balance.Press 1 To Continue Your Request : ")
                amnt = b.blnc
            if(f=='1' or b.blnc > amnt):
                b.withdraw(amnt)
    while op not in "12345":
            op = input("Enter A Valid Option                  : ")




