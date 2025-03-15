import math
import random

# K is a scaling factor determining how much a rating changes after a match
# Typically, 32 is used for low-level tournaments, and 16 for high-level
K = 32


def calc_expected_score(player_rating: int, opponent_rating: int):
    '''
    Calculates the probability of a win as a decimal rounded to 4 places
    based on their current elo, e.g. a value of 0.7597 means 'player'
    has a 75.97% chance of winning.
    '''
    expected_score = 1 / (1 + math.pow(10, (opponent_rating - player_rating) / 400)) # Elo algorithm
    expected_score = round(expected_score, 4)
    return expected_score



def update_rating(old_rating: int, actual_score: int, expected_score):
    '''
    Updates the old rating based on a new match via calc_expected_score(),
    actual_score argument is 0 for loss, 0.5 for draw, 1 for win.
    '''
    new_rating = old_rating + K * (actual_score - expected_score) # How the elo algorithm updates score via K-factor
    return round(new_rating)



def run_match(player_rating: int, opponent_rating: int):
    '''
    Simulates a match. A win adds the respective points to your elo, and vice versa for a loss.
    '''
    expected_score = round(calc_expected_score(player_rating, opponent_rating), 4)
    print(f'{expected_score * 100}% chance of winning, good luck.')
    print('Match in progress...')
    actual_result = random.random() < expected_score    # Match outcome calculated
    
    if actual_result:   # If match is won
        new_player_rating = update_rating(player_rating, 1, expected_score)
        difference = new_player_rating - player_rating
        player_rating = new_player_rating
        print(f'Match won. {difference} points have been added to your elo.\n Your new elo is {player_rating}.')
    else:               #If match is lost
        new_player_rating = update_rating(player_rating, 0, expected_score)
        difference = abs(new_player_rating - player_rating)
        player_rating = new_player_rating
        print(f'Match lost. {difference} points have been subtracted from your elo.\n Your new elo is {player_rating}.')

    play_again = input('Play again? y/n: ')
    if play_again.lower() == 'y':
        opponent_rating = int(input('What elo is your opponent? (positive int only, 0 for random): '))
        if opponent_rating == 0:
            opponent_rating = random.randrange(500, 2000)
        run_match(player_rating, opponent_rating)
    else:
        return 'Program exiting.'


# Start of program
print('Before running, the program needs to determine a K-factor.')
print('K determines the amount elo changes after a match.')
print('For a default low-level tournament setting, input 1. For a high-level tournament input 2. Otherwise specify.')
input_K = int(input('Input K-factor (positive int only): '))

# Setting K-factor
if input_K == 1:
    K = 32
elif input_K == 2:
    K = 16
else:
    K = input_K
print(f'K-factor set to {K}.')

# Setting player elo
print('Enter your current elo rating. Enter 0 to set the rating to a default of 1000.')
player_rating = int(input('Your elo: '))
if player_rating == 0:
    player_rating = 1000
print(f'Your elo has been set to {player_rating}.')

# Setting opponent elo
print('This program simulates game matches based on your above-entered rating, and updates your elo automatically.')
print("Enter your opponent's elo. Enter 0 to randomly assign their rating between 500 and 2000.")
opponent_rating = int(input('Opponent elo: '))
if opponent_rating == 0:
    opponent_rating = random.randrange(500, 2000)
print(f"Your opponent's elo has been set to {opponent_rating}.")
print('Match is beginning.')
run_match(player_rating, opponent_rating)
