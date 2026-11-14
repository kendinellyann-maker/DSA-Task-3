
def fib(n):
    if n == 0:                      
        return 0
    if n == 1:                      
        return 1
    return fib(n - 1) + fib(n - 2)  

n = int(input("Enter N: "))
print("Term", n, "of the Fibonacci series =", fib(n))