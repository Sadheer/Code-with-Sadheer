import random

def computer_choice():
    computer = ["rock", "paper", "scissors"]  # Corrected spelling of "scissors"
    comp1 = random.choice(computer)
    print("Computer choice is:", comp1)
    return comp1

while True:
    choice = input("Enter your choice (rock, paper, scissors): ").lower()
    
    if choice in ["rock", "paper", "scissors"]:  # Fixed the condition for validating the user's choice
        print("User choice is:", choice)
        computerchoice = computer_choice()
        
        if choice == computerchoice:
            print("Match tie!")
        elif (choice == "rock" and computerchoice == "scissors") or \
             (choice == "paper" and computerchoice == "rock") or \
             (choice == "scissors" and computerchoice == "paper"):
            print("You won!")
        else:
            print("You lose!")
    else:
        print("Invalid choice")
    
    play_again = input("Do you want to play again? (yes/NO): ").lower()  # Removed the extra 'r' and converted input to lowercase
    if play_again != "yes":
        print("Thank you for playing!")
        break
