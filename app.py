#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

# Creates a variable with a data structure relating each element of rock, paper, scissors to the one it beats
# This variable is used to determine the winner of the game
winning_beats = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper",
}

# Create a global variable to keep track of the score
score = [0, 0]

# Using winning_beats, create a function which determines the winner of a game of rock, paper, scissors. -1 for a tie, 0 for player 1 and 1 for player 2. Besides, record the result in the score variable
def determine_winner(player_1, player_2):
    if player_1 == player_2:
        return -1
    elif winning_beats[player_1] == player_2:
        score[0] += 1
        return 0
    else:
        score[1] += 1
        return 1

# Creates a function which given the winner, returns a string saying who won
def get_winner_string(winner):
    if winner == -1:
        return "It's a tie!"
    elif winner == 0:
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"

# Create a function which gets both players' choices in a single line using this format like this rock scissors. If the input is not in this format, it should ask again until it is
def get_choices():
    while True:
        player_1, player_2 = input("Player 1, Player 2: ").split(" ")
        if player_1 in winning_beats and player_2 in winning_beats:
            return player_1, player_2
        else:
            print("Invalid input")

# Create a function which ask the user to play again and returns True if they want to play again and False if they don't
def play_again():
    return input("Play again? (y/n) ") == "y"

# Print the final score
def print_final_score():
    print(f"Final score: Player 1: {score[0]} - Player 2: {score[1]}")

# Create a function which represent the game. At start, it should print ask the user for their choices, print the winner and ask if they want to play again. If they do, it should repeat the process. If they don't, it should print the final score and exit
def play_game():
    while True:
        player_1, player_2 = get_choices()
        winner = determine_winner(player_1, player_2)
        print(get_winner_string(winner))
        if not play_again():
            break
    print_final_score()

# Call the play_game function to start the game
play_game()
