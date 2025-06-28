import random

def hacker_guessing_game():
    tries = 0
    max_attempts = 3
    game_won = False
    
    # Generate random 4-digit number
    hacker_message = random.randint(1000, 9999)
    
    # Convert to list of digits
    lstHack = []
    temp = hacker_message
    for num in range(4):
        lstHack.insert(0, temp % 10)
        temp //= 10
    
    # Keep track of revealed positions
    revealed_positions = set()
    
    print("🔐 HACKER CHALLENGE 🔐")
    print("A 4-digit password protects the database!")
    print("You have 3 attempts to crack it.")
    print("After each wrong guess, you'll get a hint!\n")
    
    # For debugging - remove this line in final version
    print(f"[DEBUG] The answer is: {hacker_message}")
    
    while tries < max_attempts and not game_won:
        # Show current hint state
        hint_display = []
        for i in range(4):
            if i in revealed_positions:
                hint_display.append(str(lstHack[i]))
            else:
                hint_display.append("_")
        
        print(f"Current hint: {' '.join(hint_display)}")
        
        # Get user input
        curr_attempt = input("Enter your 4-digit password: ").strip()
        
        # Validate input
        if not curr_attempt.isdigit() or len(curr_attempt) != 4:
            print("Please enter exactly 4 digits!\n")
            continue
        
        # Check if correct
        if int(curr_attempt) == hacker_message:
            print("🎉 ACCESS GRANTED! You're in the database! 🎉")
            game_won = True
        else:
            tries += 1
            remaining = max_attempts - tries
            
            if remaining > 0:
                print(f"❌ Not quite! You have {remaining} attempt{'s' if remaining != 1 else ''} remaining.")
                
                # Reveal a new digit as hint
                available_positions = [i for i in range(4) if i not in revealed_positions]
                if available_positions:
                    new_reveal = random.choice(available_positions)
                    revealed_positions.add(new_reveal)
                    print(f"🔍 Hint: Position {new_reveal + 1} is '{lstHack[new_reveal]}'")
                print()
            else:
                print(f"🚫 GAME OVER! You've used all your attempts.")
                print(f"The correct password was: {hacker_message}")

# Run the game
if __name__ == "__main__":
    hacker_guessing_game()