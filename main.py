# arcade.py

import argparse
import sys
import guessnumber
import r_p_s
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
        guessnumber()
    elif choose == '2':
        r_p_s()
    elif choose == '3':
        run_snake_game()
    elif choose == '4':
        print("Thanks for playing! Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a valid option.")
