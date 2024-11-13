import random

def get_user_choice():
    """Get the user's choice (rock, paper, or scissors)."""
    user_choice = input("Enter rock, paper, or scissors: ").lower()
    while user_choice not in ["rock", "paper", "scissors"]:
        user_choice = input("Invalid choice. Please enter rock, paper, or scissors: ").lower()
    return user_choice

def get_computer_choice():
    """Randomly generate the computer's choice."""
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """Determine the winner of the game."""
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "win"
    else:
        return "lose"

def update_stats(result, stats):
    """Update the stats dictionary based on the result."""
    if result == "win":
        stats["wins"] += 1
    elif result == "lose":
        stats["losses"] += 1
    else:
        stats["ties"] += 1

def display_stats(stats):
    """Display the current stats."""
    total_games = stats["wins"] + stats["losses"] + stats["ties"]
    if total_games > 0:
        win_percentage = (stats["wins"] / total_games) * 100
        print(f"\nGame Stats: Wins: {stats['wins']}, Losses: {stats['losses']}, Ties: {stats['ties']}")
        print(f"Win Percentage: {win_percentage:.2f}%")
    else:
        print("No games played yet.")

def play_game():
    """Play multiple rounds of rock-paper-scissors and track stats."""
    stats = {"wins": 0, "losses": 0, "ties": 0}
    
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        
        print(f"Computer chose: {computer_choice}")
        
        if result == "tie":
            print("It's a tie!")
        elif result == "win":
            print("You win!")
        else:
            print("You lose!")
        
        update_stats(result, stats)
        display_stats(stats)
        
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break

# Main function to run the game
if __name__ == "__main__":
    play_game()
