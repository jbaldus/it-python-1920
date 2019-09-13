# Write your code here :-)
import random
#from banner import banner

def print_title():
    print("Fire, Water, Wood: An epic game of domination!")
    print("")
    print("""
In this game, you are the master of a trio of monsters
that live in your pocket. They are called Monstepoks. Each
Monstepok is powered by a different elemental power. Fire
Monstepoks harness the destructive force of fire, but can be
defeated by Monstepoks that channel the flowing nature of
water. Water Monstepoks are devoured by Wood Monstepoks, who
get their power from the life-force of trees and plants. Wood
Monstepoks are vulnerable to Fire Monstepoks, though.""")
    print("")

def print_menu():
    print("You may choose to order any of these Monstepoks into battle")
    print("1. Lavamander (Fire) - A gecko made of lava.")
    print("2. Sharkpuncher (Water) - A shark with arms and legs who likes to punch.")
    print("3. Entrotree (Wood) - An ancient tree person.")
    print("")
    choice = int(input("Please enter the number of your choice and press <Enter>: "))

    return choice

def print_score(player, computer):
    print("")
    print("+---------[SCORE]---------+")
    print(f"| Player: {player}   Charcoal: {computer} |")
    print("+-------------------------+")
    print("")

def main():
    print_title()
    print("Your long-time rival, Charcoal, has arrived! They challenge you to 3 battles!")
    print("The player who wins two battles will be victorious")
    player_wins = 0
    computer_wins = 0
    while player_wins < 2 and computer_wins <2:
        print_score(player_wins, computer_wins)
        player_choice = print_menu()
        computer_choice = random.randint(1,3)
        print("")
        if player_choice == 1:
            if computer_choice == 1:
                print("Charcoal also chooses Lavamander. Your two Lavamanders fight for "
                      "days without either one gaining an advantage. Eventually, a storm "
                      "comes and the rain cools them down. Now they are friends. This "
                      "match is a tie.\n")
            elif computer_choice == 2:
                print("Charcoal chose Sharkpuncher, who douses your Lavamander with water "
                      "turning it to stone. You lose this round.\n")
                computer_wins = computer_wins + 1
            else:
                print("Charcoal chose Entrotree, and your Lavamander shoots lava at it, "
                      "burning it to a crisp. You win this round.\n")
                player_wins = player_wins + 1
        elif player_choice == 2:
            if computer_choice == 1:
                print("Charcoal foolishly chose Lavamander. Your Sharkpuncher quenches "
                      "Lavamander and turns it to a statue. You win this round.\n")
                player_wins = player_wins + 1
            elif computer_choice == 2:
                print("Sharkpunchers love to punch. Charcoal also chose Sharkpuncher, "
                      "and your two Sharkpunchers punched each other until they fell in "
                      "love. This round is a  Tie.\n")
            else:
                print("Charcoal chose Entrotree. Entrotree plants it's roots in your Sharkpuncher's "
                      "fist and pulls all of the water out of it's body, leaving you with a dessicated "
                      "Sharkpuncher.\n")
                computer_wins = computer_wins + 1
        else:
            if computer_choice == 1:
                print("Charcoal chose Lavamander. Their Lavamander jumps on your Entrotree, "
                      "burning it to a crisp. Charcoal says, \"That's why they call me Charcoal!\""
                      "You lose this round.\n")
                computer_wins = computer_wins + 1
            elif computer_choice == 2:
                print("Charcoal chose Sharkpuncher. Sharkpunchers punches do little damage to "
                      "your Entrotree, and eventually Entrotree's bark captures a punch and "
                      "envelops Charcoal's Sharkpuncher, draining it from all the water in "
                      "it's body. You win this round.\n")
                player_wins = player_wins + 1
            else:
                print("Charcoal also chose Entrotree. Your Entrotree hasn't seen another "
                      "Entrotree for as long as it can remember, and neither has Charcoal's. "
                      "Instead of fighting, they embrace each other and go out for a coffee "
                      "to catch up. This round is a tie.\n")
        input("\nPress <Enter> to continue...")
        print("")

    # We're done playing at this point
    if player_wins == 2:
        print("")
        print("""
You have destroyed your rival, Charcoal. They run away in tears, vowing to enslave stronger Monstepoks
and defeat you next time. """)
    else:
        print("""
You have been ruthlessly crushed by your rival, Charcoal. They tease you until you run away in tears, resolving
yourself to enslave stronger Monstepoks and return to defeat Charcoal next time.""")




main()