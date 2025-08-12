import random

def play_game():
    # Define choices
    choices = ["rock", "paper", "scissors"]

    # Scores
    user_score = 0
    computer_score = 0
    rounds = 5
    current_round = 1

    print("\n🎮 Welcome to Rock, Paper, Scissors!")
    print("First to win best of 5 rounds.\n")

    while current_round <= rounds:
        print(f"Round {current_round} of {rounds}")
        user_input = input("Choose rock, paper or scissors: ").lower()

        if user_input not in choices:
            print("Invalid choice. Try again.\n")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        if user_input == computer_choice:
            print("It's a draw!\n")
        elif (user_input == "rock" and computer_choice == "scissors") or \
             (user_input == "paper" and computer_choice == "rock") or \
             (user_input == "scissors" and computer_choice == "paper"):
            print("You win this round!\n")
            user_score += 1
        else:
            print("Computer wins this round!\n")
            computer_score += 1

        current_round += 1

    # Final result
    print("Game Over!")
    print(f"Final Score - You: {user_score} | Computer: {computer_score}")

    if user_score > computer_score:
        print("Congratulations, you won!")
    elif computer_score > user_score:
        print("Better luck next time!")
    else:
        print("It's a tie!")

# Main loop to ask for replay
while True:
    play_game()
    again = input("\nDo you want to play another round? (Y/N): ").strip().lower()
    if again != "y":
        print("Thanks for playing! Goodbye 👋")
        break
