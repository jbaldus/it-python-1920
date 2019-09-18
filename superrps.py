import random
from banner import banner
banner("SUPERRPS", "Mr. Baldus")

options=["Fire", "Wood", "Poison", "Water"]

def get_player_choice(options):
    for num, text in enumerate(options):
        print(f"{num}. {text}")
    choice = int(input("What is your choice? "))
    print("")
    return choice

def get_winner(p1: int, p2: int):
    global options
    winner = None
    if (p2 + 1) % len(options) == p1:
        winner = 2
    elif (p1 + 1) % len(options) == p2:
        winner = 1
    return winner

def print_welcome(options):
    print(f"We are going to play {', '.join(options)}.")
    print(f"In this game {' beats '.join(options)}, which beats {options[0]}.")
    print("")


def print_score(p1, p2):
    scoreline = f" Player 1: {p1}   Player 2: {p2} "
    title = "SCoRE-BOaRD"
    print("")
    print(f"+{f'[{title}]':-^{len(scoreline)}}+")
    print(f"|{scoreline}|")
    print(f"+{'-'*len(scoreline)}+")
    print("")

def main():
    global options
    print_welcome(options)

    print_score(251,1)

    while True:
        p1_choice = get_player_choice(options)
        p2_choice = get_player_choice(options)

        winner = get_winner(p1_choice, p2_choice)
        print(f"Player 1 chose {options[p1_choice]}. Player 2 chose {options[p2_choice]}.")
        if winner:
            print(f"The winner is Player {winner}")
        else:
            print("This round is a tie!")

main()