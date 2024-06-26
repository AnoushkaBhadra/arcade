# arcade.py

import argparse
import sys
from guessnumber import guess_the_number_game
from r_p_s import rock_paper_scissors_game
from snake_game import run_snake_game

parser = argparse.ArgumentParser(
    description="Arcade Game Selector"
)
parser.add_argument(
    '-n', '--name', metavar="name",
    required=False, default="User", help="Enter the name of the player"
)
args = parser.parse_args()
name = args.name

while True:
    choose = input(f"Hello! {name}, welcome to the \"ARCADE\"🕹️!\nPress 1 to play \"Guess The Number\"\nPress 2 to play \"Rock Paper Scissors\"\nPress 3 to play \"Snake Game\"\nPress 4 to Exit\n")

    if choose == '1':
        guess_the_number_game(name)
    elif choose == '2':
        rock_paper_scissors_game(name)
    elif choose == '3':
        run_snake_game()
    elif choose == '4':
        print("Thanks for playing! Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a valid option.")
