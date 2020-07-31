# show alternate character
ii = 'Hello world'
print(ii[0:16:3])  # Output -> Hlowrd
# Reverse string
xx = "Hello World"
# After second colon number is negative then it return reverse string
print(xx[::-1])  # Output ->  dlrow olleH
print(xx[::-2])  # Output -> drWolH
print(xx.endswith('ld'))  # Output -> True
print(xx.replace('World', 'Sandip'))  # Output -> Hello Sandip
# In above eg. first reverse string then return alternate character

x = '23'
print(int(x) + 10) # This is Typecasting
print('Sandip\t' * 10)  # Output -> Sandip	Sandip	Sandip	Sandip	Sandip	Sandip	Sandip	Sandip	Sandip	Sandip
# User enter two number and there addition
i = input('Enter Your first number? ')
x = input('Enter your second number? ')
print('You have enter', int(i), int(x))
print('Addition of two number is ', int(i) + int(x))
print(len(ii.upper()))

# F string
a = 'our'
b = 'World'
print(f'Welcome to {a} {b}')  # Output -> Welcome to our World