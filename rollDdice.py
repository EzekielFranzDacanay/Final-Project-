import random

def roll_dice():
    """Simulates rolling a 6-sided dice."""
    return random.randint(1, 6)

def play_dice_game():
    """Simulates a thrilling dice duel between two players."""
    player1_score = 0
    player2_score = 0
    rounds_played = 0
    
    print("Welcome to the Epic Dice Duel!")
    print("The victor will be the first to achieve 2 victories out of 3 rounds.")
    
    while player1_score < 2 and player2_score < 2:
        rounds_played += 1
        print(f"\n--- Round {rounds_played} ---")
        
        input(f"Player 1: Press Enter to roll your dice.")
        player1_roll = roll_dice()
        print(f"Player 1 rolls: {player1_roll}")
        
        input(f"Player 2: Press Enter to roll your dice.")
        player2_roll = roll_dice()
        print(f"Player 2 rolls: {player2_roll}")
        
        if player1_roll > player2_roll:
            player1_score += 1
            print("Player 1 triumphs this round!")
        elif player2_roll > player1_roll:
            player2_score += 1
            print("Player 2 triumphs this round!")
        else:
            print("It's a tie for this round!")
        
        print(f"Score after Round {rounds_played}:")
        print(f"Player 1: {player1_score} victory(s)")
        print(f"Player 2: {player2_score} victory(s)")
    
    if player1_score == 2:
        print("\nHooray! Player 1 emerges victorious in the thrilling dice duel.")
    else:
        print("\nHooray! Player 2 emerges victorious in the thrilling dice duel.")

# Run the game
play_dice_game()
