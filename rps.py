import random
from banner import banner
banner("ROCK, PAPER, SCISSORS", "Mr. Baldus")

def print_title():
    print("We are going to play Rock, Paper, Scissors. The first to win two out of three rounds is the winner.")
    print("")

def print_menu():
    choice = None
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("")
    while choice is None:
        try:
            choice = int(input("What is your choice?  "))
        except ValueError:
            print("Please enter the number of your choice.")


    return choice

def print_score(player, computer):
    print("")
    print(f"Score:  Player: {player} Computer: {computer}")
    print("")

def main():
    print_title()
    player_wins = 0
    computer_wins = 0
    while player_wins < 2 and computer_wins <2:
        print_score(player_wins, computer_wins)
        player_choice = print_menu()
        computer_choice = random.randint(1,3)
        print("")
        if player_choice == 1:
            if computer_choice == 1:
                print("You chose Rock, and the computer chose Rock. It is a tie.\n")
            elif computer_choice == 2:
                print("You chose Rock, and the computer chose Paper. You lose this round.\n")
                computer_wins = computer_wins + 1
            else:
                print("You chose Rock, and the computer chose Scissors. You win this round.\n")
                player_wins = player_wins + 1
        elif player_choice == 2:
            if computer_choice == 1:
                print("You chose Paper, and the Computer chose Rock. You win this round.\n")
                player_wins = player_wins + 1
            elif computer_choice == 2:
                print("You chose Paper, and the Computer chose Paper. This round is a tie.\n")
            else:
                print("You chose Paper, and the Computer chose Scissors. You lose this round.\n")
                computer_wins = computer_wins + 1
        elif player_choice == 3:
            if computer_choice == 1:
                print("You chose Scissors, and the Computer chose Rock. You lose this round.\n")
                computer_wins = computer_wins + 1
            elif computer_choice == 2:
                print("You chose Scissors, and the Computer chose Paper. You win this round.\n")
                player_wins = player_wins + 1
            else:
                print("You chose Scissors, and the Computer chose Scissors. This round is a tie.\n")
        else:
            print("You must choose a number from 1 to 3. Please Try again!")
            continue


    # We're done playing at this point
    if player_wins == 2:
        print("")
        print("You have defeated the computer in honorable battle! It was pure hubris for the computer \n"
              "to think it could win against such a formidable opponent. Congratulations! ")
    else:
        print("You have been ruthlessly crushed by the computer. You should never have tried to outsmart \n"
              "the computer at choosing randomly."
              "Better luck next time!")




main()