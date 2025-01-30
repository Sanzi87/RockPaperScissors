import random

ROCK = 'r'
PAPER = 'p'
SCISSORS = 's'

emojis = {ROCK: '🤜', PAPER: '🤚', SCISSORS: '✌️'}
choices = tuple(emojis.keys())


def get_user_choice():
    while True:
        user_choice = input(
            f'Rock, paper, or scissors? ({ROCK}/{PAPER}/{SCISSORS}): ').lower()
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
    elif (
        (user_choice == ROCK and computer_choice == SCISSORS) or
        (user_choice == SCISSORS and computer_choice == PAPER) or
            (user_choice == PAPER and computer_choice == ROCK)):
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
