import random

emojis = {'r': '🤜', 'p': '🤚', 's': '✌️'}
choices = ('r', 'p', 's')


def get_user_choice():
    while True:
        user_choice = input('Rock, paper, or scissors? (r/p/s): ').lower()
        # If choice is valid
        if user_choice in choices:
            return user_choice
        else:
            # Print an error
            print('Invalid choice!')
            # continue


def display_choices(user_choice, computer_choice):
    print(f'You chose {emojis[user_choice]}')
    print(f'Computer chose {emojis[computer_choice]}')


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print('Tie!')
    elif (user_choice == 'r' and computer_choice == 's') or (user_choice == 's' and computer_choice == 'p') or (user_choice == 'p' and computer_choice == 'r'):
        print('You win!')
    else:
        print('You lose!')


def play_game():
    while True:
        # Ask the user to make a choice
        user_choice = get_user_choice()

        # Let the computer to make a choice
        computer_choice = random.choice(choices)

        # Print choices
        display_choices(user_choice, computer_choice)

        # Determine the winner
        determine_winner(user_choice, computer_choice)

        # Ask the user if he want to continue
        should_continue = input('Continue? (y/n: ').lower()
        # If not
        if should_continue == 'n':
            # Terminate
            break


play_game()
