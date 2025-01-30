import random

emojis = {'r': '🤜', 'p': '🤚', 's': '✌️'}
choices = ('r', 'p', 's')

while True:
    # Ask the user to make a choice
    user_choice = input('Rock, paper, or scissors? (r/p/s): ').lower()
    # If choice is not valid
    if user_choice not in choices:
        # Print an error
        print('Invalid choice!')
        continue

    # Let the computer to make a choice
    computer_choice = random.choice(choices)

    # Print choices
    print(f'You chose {emojis[user_choice]}')
    print(f'Computer chose {emojis[computer_choice]}')

    # Determine the winner
    if user_choice == computer_choice:
        print('Tie!')
    elif (user_choice == 'r' and computer_choice == 's') or (user_choice == 's' and computer_choice == 'p') or (user_choice == 'p' and computer_choice == 'r'):
        print('You win!')
    else:
        print('You lose!')

    # Ask the user if he want to continue
    should_continue = input('Continue? (y/n: ').lower()
    # If not
    if should_continue == 'n':
        # Terminate
        break
