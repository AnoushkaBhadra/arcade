import random
import math

def guess_the_number_game(name):
    print(f"Hello! {name}, welcome to \"GUESS THE NUMBER\" game!")
    round = 0
    win = 0

    start = input("Would you like to start? (Y/N) \n")

    if start.lower() == "y":
        while True:
            num = random.randrange(1, 4)
            user_input = int(input(f"{name}, choose a random number between 1, 2, or 3... \n"))

            if user_input == num:
                print(f"🎉 {name}, you guessed the correct number!")
                win += 1
            else:
                print("Oh no! 😢 You guessed the wrong number")

            round += 1
            percentage = (win / round) * 100
            print(f"Winning rate: {math.floor(percentage)}%")
            print(f"Rounds played: {round}")

            reply = input("Would you like to continue? (Y/N) \n")
            if reply.lower() != "y":
                break

    print("Returning to the arcade. Thanks for playing!")

if __name__ == '__main__':
    name = input("Enter your name: ")
    guess_the_number_game()