yr=int(input("Enter An Year : "))
if yr%400 == 0 or ( yr%100 != 0 and yr%4 == 0 ):
    print(yr," Is A Leap Year")
else:
    print(yr," Is Not A Leap Year")