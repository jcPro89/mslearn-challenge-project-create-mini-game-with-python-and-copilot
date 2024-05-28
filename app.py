# this is a rock, paper, scissors game
# the user will play against the computer
# the computer will randomly select rock, paper, or scissors
# the user will be prompted to select rock, paper, or scissors
# the computer will compare the user's selection to its own selection
# and determine the winner. the game will inform the player if they won, lost, or tied
# the user will be prompted to play again or quit

import random

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True) # run the server in debug mode 



def main():
    playerScore = 0  # Inicializar playerScore
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        user_choice = input("Enter rock, paper, or scissors: ").lower()
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = random.choice(["rock", "paper", "scissors"])
        print(f"Computer chose {computer_choice}")

        if user_choice == computer_choice:
            # tie
            print("It's a tie!")
        elif user_choice == "rock":
            # user chose rock
            if computer_choice == "scissors":
                print("You win!")
                playerScore += 1  # Incrementar playerScore si el jugador gana                
            else:
                print("You lose!")
        elif user_choice == "paper":
            # user chose paper
            if computer_choice == "rock":
                print("You win!")
                playerScore += 1  # Incrementar playerScore si el jugador gana
            else:
                print("You lose!")
        elif user_choice == "scissors":
            # user chose scissors
            if computer_choice == "paper":
                print("You win!")
                playerScore += 1  # Incrementar playerScore si el jugador gana
            else:
                print("You lose!")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print(f"Your score is: {playerScore}")  # Mostrar playerScore cuando el jugador decida no jugar más
            break

    print("Thanks for playing!")
    
    
    
if __name__ == '__main__':
    main()