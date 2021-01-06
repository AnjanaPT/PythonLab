def Sum_list(n):
    s = 0
    for i in n:
        s += i
    return(s)
l = input("Enter The Numbers : ")
lst = list(map(int,l.split()))
print("Sum Of Elements In The List Is : ",Sum_list(lst))