
import random

def rock_paper_scissors_game():
    """Rock Paper Scissors game following the flowchart logic"""
    
    # Initialize scores
    user_score = 0
    computer_score = 0
    
    print("=== ROCK PAPER SCISSORS GAME ===")
    print("Follow the flowchart logic!")
    print("-" * 35)
    
    while True:
        # User selects: Rock, Paper, or Scissors
        print("\nChoose your weapon:")
        print("1. Rock")
        print("2. Paper") 
        print("3. Scissors")
        
        try:
            user_choice = input("Enter your choice (1-3): ").strip()
            
            # Validate input
            if user_choice not in ['1', '2', '3']:
                print("Invalid choice! Please enter 1, 2, or 3.")
                continue
            
            # Convert to text
            choices = {
                '1': 'rock',
                '2': 'paper',
                '3': 'scissors'
            }
            
            user_weapon = choices[user_choice]
            
            # Computer generates: Rock, Paper, or Scissors
            computer_weapon = random.choice(['rock', 'paper', 'scissors'])
            
            print(f"\nYou chose: {user_weapon.upper()}")
            print(f"Computer chose: {computer_weapon.upper()}")
            
            # Compare user's choice to computer's choice and calculate scores
            if user_weapon == computer_weapon:
                # If user = computer score (tie)
                print("It's a TIE! No points awarded.")
            elif (user_weapon == 'rock' and computer_weapon == 'scissors') or \
                 (user_weapon == 'paper' and computer_weapon == 'rock') or \
                 (user_weapon == 'scissors' and computer_weapon == 'paper'):
                # User wins this round
                user_score += 1
                print("🎉 You WIN this round!")
            else:
                # Computer wins this round
                computer_score += 1
                print("💻 Computer WINS this round!")
            
            # Display current scores
            print(f"\nCurrent Scores:")
            print(f"You: {user_score}")
            print(f"Computer: {computer_score}")
            
            # Check if user scores > computer (overall winner)
            if user_score > computer_score:
                print("🏆 You are currently LEADING!")
            elif computer_score > user_score:
                print("😅 Computer is currently LEADING!")
            else:
                print("🤝 It's currently TIED!")
            
            # Play again?
            play_again = input("\nDo you want to play again? (yes/no): ").lower().strip()
            
            if play_again not in ['yes', 'y']:
                break
                
        except KeyboardInterrupt:
            print("\n\nGame interrupted by user.")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Please try again.")
    
    # End - Final Results
    print("\n" + "="*40)
    print("GAME OVER - FINAL RESULTS")
    print("="*40)
    print(f"Your final score: {user_score}")
    print(f"Computer final score: {computer_score}")
    
    # Determine overall winner
    if user_score > computer_score:
        print("🎉🏆 YOU ARE THE OVERALL WINNER! 🏆🎉")
    elif computer_score > user_score:
        print("💻🏆 COMPUTER IS THE OVERALL WINNER! 🏆💻")
    else:
        print("🤝 IT'S A TIE OVERALL! 🤝")
    
    print("Thanks for playing!")

def best_of_rounds():
    """Play best of X rounds"""
    
    print("=== BEST OF X ROUNDS ===")
    
    try:
        rounds = int(input("How many rounds to play? (odd number recommended): "))
        
        if rounds <= 0:
            print("Number of rounds must be positive. Setting to 3.")
            rounds = 3
            
    except ValueError:
        print("Invalid input. Setting to 3 rounds.")
        rounds = 3
    
    user_score = 0
    computer_score = 0
    round_count = 0
    
    while round_count < rounds:
        round_count += 1
        print(f"\n--- ROUND {round_count} of {rounds} ---")
        
        try:
            # User selects
            user_choice = input("Choose (rock/paper/scissors): ").lower().strip()
            
            if user_choice not in ['rock', 'paper', 'scissors']:
                print("Invalid choice! Skipping round.")
                round_count -= 1
                continue
            
            # Computer generates
            computer_choice = random.choice(['rock', 'paper', 'scissors'])
            
            print(f"You: {user_choice}")
            print(f"Computer: {computer_choice}")
            
            # Compare and calculate scores
            if user_choice == computer_choice:
                print("Tie!")
            elif (user_choice == 'rock' and computer_choice == 'scissors') or \
                 (user_choice == 'paper' and computer_choice == 'rock') or \
                 (user_choice == 'scissors' and computer_choice == 'paper'):
                user_score += 1
                print("You win this round!")
            else:
                computer_score += 1
                print("Computer wins this round!")
            
            print(f"Score: You {user_score} - {computer_score} Computer")
            
        except KeyboardInterrupt:
            print("\n\nGame interrupted by user.")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Skipping this round.")
            round_count -= 1
    
    # Final winner determination
    print(f"\nFINAL SCORE: You {user_score} - {computer_score} Computer")
    if user_score > computer_score:
        print("🎉 YOU WIN THE GAME!")
    elif computer_score > user_score:
        print("💻 COMPUTER WINS THE GAME!")
    else:
        print("🤝 IT'S A TIE!")

# Run the game
if __name__ == "__main__":
    print("🎮 WELCOME TO ROCK PAPER SCISSORS! 🎮")
    print("Choose game mode:")
    print("1. Continuous play (following flowchart)")
    print("2. Best of X rounds")
    
    try:
        mode = input("Enter 1 or 2: ").strip()
        
        if mode == "1":
            rock_paper_scissors_game()
        elif mode == "2":
            best_of_rounds()
        else:
            print("Invalid choice. Starting continuous play...")
            rock_paper_scissors_game()
            
    except KeyboardInterrupt:
        print("\n\nThanks for playing!")
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Starting default game...")
        rock_paper_scissors_game()
                                