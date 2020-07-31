# Snake Water Gun
# Snake - Water = Snake win
# Gun - Snake = Gun win
# other combination are draw
import random
i = 1
user_counts = 0
comp_counts = 0
while i < 11:
    a = ['s', 'w', 'g']
    print("----Enter your choice---- \n 's' for Snake \n 'w' for Water \n 'g' for Gun")
    user_input = input().lower()
    comp_input = random.choice(a)
    while user_input not in ('s','w','g'):
        print('\n----Invalid input. Please enter a right input----\n')
        print("----Enter your choice---- \n 's' for Snake \n 'w' for Water \n 'g' for Gun")
        user_input = input().lower()
    print(f'User Input = {user_input} || Computer Input  = {comp_input}')
    if user_input == 's':
        if comp_input == 'w':
            user_counts += 1
        elif comp_input == 'g':
            comp_counts += 1
    elif user_input == 'g':
        if comp_input == 's':
            user_counts += 1
    i += 1
    print('User points =', user_counts, end=' || ')
    print('Computer points = ', comp_counts)
if user_counts > comp_counts:
    print("\n-----User WINNER-----")
    print('User points =', user_counts, end=' || ')
    print('Computer points = ', comp_counts)
elif comp_counts > user_counts:
    print('Computer WINNER')
    print('User points =', user_counts, end=' || ')
    print('Computer points = ', comp_counts)
else:
    print("Game Draw")
    print('User points =', user_counts, end=' || ')
    print('Computer points = ', comp_counts)
