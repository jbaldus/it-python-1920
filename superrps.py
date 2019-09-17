options=["Fire", "Wood", "Poison", "Water"]

def get_player_choice():
    global options
    for num, text in enumerate(options):
        print(f"{num}. {text}")
    choice = int(input("What is your choice? "))
    return choice
