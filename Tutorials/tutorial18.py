# Built in functions
a = [2,5,2,5,2,1,1,33,55,555]
print(min(a))
print(max(a))
print(sorted(a))
print(sum(a))
print(len(a))
print(type(a))

# Built in methods

# strip() - if the string has whitespaces at the beginning or at the end of the string, it removes them.


# join() function
x = ['John','Cena','Randy','Orton','Khali']
a = ' , '.join(x)
print(a)  # Output -> John , Cena , Randy , Orton , Khali

# function that filters vowels
letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o']
def filtervowels(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']

    if(letter in vowels):
        return True
    else:
        return False

filteredvowels = filter(filtervowels, letters)

print('The filtered vowels are:')
for vowel in filteredvowels:
    print(vowel)

#Even number
lis = [1, 2, 3, 4, 5,46,3,2,44,2,22,3,3,565,3]
out = []
for num in lis:
    if num % 2 == 0:
        out.append(num)
print(out)

# Even number using Lambda function
lis1 = [1, 2, 3, 4, 5]
is_even = lambda x: x % 2 == 0
lis2 = list(filter(is_even, lis1))
print(lis2)

# random method
# random.choice - use for random value selected
import random
a = ['Snake','Water','Gun']
print('random value',random.choice(a))