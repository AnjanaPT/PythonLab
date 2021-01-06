def fib(n):
    a = c = 0
    b = 1
    for i in range(n):
        print(c, end=' ')
        c = a + b
        a = b
        b = c
n = int(input("Enter The Number Of Terms : "))
fib(n)