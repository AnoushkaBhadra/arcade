import random
import math

def rock_paper_scissors_game(name):
    print(f"Hello! {name}, welcome to the classic \"ROCK, PAPER, SCISSOR\" game!")
    moves = ["rock", "paper", "scissor"]
    winning_conditions = {
        "rock": "scissor",
        "paper": "rock",
        "scissor": "paper"
    }
    rounds = 0
    wins = 0
    ties = 0

    start = input("Would you like to start? (Y/N) \n")

    if start.lower() == "y":
        while True:
            player_move = input("Enter your move: (Rock/Paper/Scissor): ").lower()
            system_move = random.choice(moves)

            if player_move not in moves:
                print("Invalid move! Please enter Rock, Paper, or Scissor.")
                continue

            print(f"{name} plays {player_move}!")
            print(f"Python 🐍 plays {system_move}!")

            if player_move == system_move:
                print("It's a tie!")
                ties += 1
            elif winning_conditions[player_move] == system_move:
                print("Yay! You win! 🎉")
                wins += 1
            else:
                print("Oh no! 😥 You lose!")

            rounds += 1
            win_rate = (wins / rounds) * 100
            print(f"Winning rate: {math.floor(win_rate)}%")
            print(f"Ties: {ties}")
            print(f"Rounds played: {rounds}")

            reply = input("Would you like to continue? (Y/N) \n")
            if reply.lower() != "y":
                break

    print("Returning to the arcade. Thanks for playing!")
if __name__ == '__main__':
    name = input("Enter your name: ")
    rock_paper_scissors_game(name)