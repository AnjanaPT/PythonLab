def Sum_list(n):
    s = 0
    for i in n:
        s += i
    return(s)
lst = map(float,input("Enter The Numbers : ").split())
print("Sum Of Elements In The List Is : ",Sum_list(lst))