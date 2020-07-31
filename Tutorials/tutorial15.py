# Recursive Vs Iterative
# Factorial using Iterative method
# n! = n * n-1 * n-2 * n-3 *......1
# n! = n * (n-1)!
def factorial_interative(n):
    fact = 1
    for i in range(n):
        fact = fact * (i+1)
    return fact

# Factorial using Recursive method
def factorial_recursive(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n-1)


print("Enter a number")
get_no = int(input())
print("Result in factorial interative method : ", factorial_interative(get_no))
print("Result in factorial recursive method : ", factorial_recursive(get_no))

