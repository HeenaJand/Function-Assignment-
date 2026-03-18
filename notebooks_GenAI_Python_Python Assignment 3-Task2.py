##Task2 Recursive Function: Factorial Utility 

def factorial(n):
    if n < 0:
        print("*****Error*****: Factorial can't be evaluate for negative number")
        return None
    if n==0 or n==1:
     return 1
    
    return n*factorial(n-1)
print("Factorial of 5:",factorial(5))
print("Factorial of 0:",factorial(0))
print("Factorial of -3",factorial(-3))



