# Factorial of n
n = int(input("Enter the number u wanna find the factorial of:\n"))
def factorial():
    """
    This function gives u the factorial of any desired number
    """
    global n
    for i in range(n-1,1,-1):
        n = n*i
    print(n)
factorial()
print(factorial.__doc__)
#recursion is when a function calls itself





#Fibonacci 
number=int(input("Enter a number:\n"))
def fibonacci(n):
    a = 0
    b = 1
    
    for i in range(0,n):
        c = a + b
        a = b
        b = c
        print(c)

fibonacci(number)