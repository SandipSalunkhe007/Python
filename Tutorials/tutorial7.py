# Guess the number with Limited chances
guess = 18
times = 9
while times > 0:
    user_val = int(input('Enter a number\n'))

    if user_val > 18:
        print('Value is greater than guess value')
    elif user_val < 18:
        print('Value is less than guess value')
    else:
        print('Guess number is correct')
        print('Number of the guesses he took to finish ', 10 - times)
        break
    times = times - 1
    print('No. of guesses left ',times)
else:
    print('Game over')