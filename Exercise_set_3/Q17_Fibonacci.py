def fib(n):
    a,b = 0,1
    for i in range(n):
        print(a, end=' ')
        a,b=b,a+b
n = int(input("Enter The Number Of Terms : "))
print("First ",n,"Terms In The Fibonacci Series Are : ",end=" ")
fib(n)