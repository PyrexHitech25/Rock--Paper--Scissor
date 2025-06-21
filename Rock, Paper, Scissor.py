import random
from time import sleep

game_choice = ["Scissor", "Rock", "Paper"]
ki = random.choice(game_choice)

print("Welcome to my Rock-Paper-Scissor Game! :)\n")

sleep(1)

def options():
    print("(1) Rock\n"
          "(2) Paper\n"
          "(3) Scissor\n")
options()

sleep(1)

def game():
    # Lose Block

    if player_choice == 1 and ki == "Paper":
        print(f"You lose! I got :) {ki}!")
    elif player_choice == 2 and ki == "Scissor":
        print(f"You lose! I got :) {ki}!")
    elif player_choice == 3 and ki == "Rock":
        print(f"You lose! I got :) {ki}!")

    # Win Block

    elif player_choice == 1 and ki == "Scissor":
        print(f"You win! I got :) {ki}!")
    elif player_choice == 2 and ki == "Rock":
        print(f"You win! I got :) {ki}!")
    elif player_choice == 3 and ki == "Paper":
        print(f"You win! I got :) {ki}!")

    # Higher than 3

    elif player_choice > 3:
        print("\nPlease name a valid option\n")


    # Tie

    else:
        print(f"Its a tie! I also got :) {ki}")


while True:
    try:
        player_choice = int(input("Choose one! :)\n"))
        if player_choice in (1, 2, 3):
            print("Thinking......\n")
            sleep(1)
            game()
            sleep(1)
            again = int(input("\nDo you wanna try again? Yes = 1 or No = 2\n"))
            sleep(1)
            try:
                if again == 1:
                    continue
                elif again == 2:
                    sleep(1)
                    print("\nThanks for playing! \n")
                    sleep(1)
                    break
                else:
                    print("1 or 2 please")
                    continue
            except ValueError:
                print("Please type 1 or 2! ")


    except ValueError:
        sleep(1)
        print("\nThinking.....\n")
        sleep(1)
        print("That's no number! :D try again\n")
        sleep(1)
        options()
        False
