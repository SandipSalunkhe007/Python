# Fibonacci sequence
# 0 1 1 2 3 5 8 13 21 ....
# In that sequence last two number addition and start with 0 and 1
# start with 0 and 1 and next number is addition of previous two number

def fibonacci(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonacci(number -1) + fibonacci(number - 2)

result = fibonacci(6)
print(result)  # Output -> 8