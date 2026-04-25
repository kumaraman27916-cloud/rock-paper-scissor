import random

# Function for Stone-Paper-Scissors
def stone_paper_scissors():
    choices = ["stone", "paper", "scissors"]
    
    user = input("Enter stone, paper, or scissors: ").lower()
    computer = random.choice(choices)
    
    print("Computer chose:", computer)
    
    if user == computer:
        print("It's a tie!")
    elif (user == "stone" and computer == "scissors") or \
         (user == "paper" and computer == "stone") or \
         (user == "scissors" and computer == "paper"):
        print("You win!")
    elif user in choices:
        print("Computer wins!")
    else:
        print("Invalid choice!")

# Function for Dice Roll Game
def dice_roll_game():
    user_roll = random.randint(1, 6)
    computer_roll = random.randint(1, 6)
    
    print("You rolled:", user_roll)
    print("Computer rolled:", computer_roll)
    
    if user_roll > computer_roll:
        print("You win!")
    elif user_roll < computer_roll:
        print("Computer wins!")
    else:
        print("It's a tie!")

# Main menu function
def main():
    while True:
        print("\n--- GAME MENU ---")
        print("1. Stone Paper Scissors")
        print("2. Dice Roll Game")
        print("3. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            stone_paper_scissors()
        elif choice == 2:
            dice_roll_game()
        elif choice == 3:
            print("Exiting game...")
            break
        else:
            print("Invalid choice!")

# Run program
main()