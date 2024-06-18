import random

def generate_computer_choice():
    """Randomly select between 'rock', 'paper', and 'scissors' for the computer."""
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(player1, Computerbot):
    """Determine the winner based on the choices made."""
    if player1 == Computerbot:
        return 'tie'
    elif (player1 == 'rock' and Computerbot == 'scissors') or \
         (player1 == 'scissors' and Computerbot == 'paper') or \
         (player1 == 'paper' and Computerbot == 'rock'):
        return 'player'
    else:
        return 'computer'

def rock_paper_scissors():
    """Play a best-of-three Rock, Paper, Scissors game."""
    player_wins = 0
    computer_wins = 0
    rounds = 0
    
    print("Welcome to the Rock, Paper, Scissors Game!")
    print("Let's see who can win two rounds first!")

    while player_wins < 2 and computer_wins < 2:
        player1 = input("Enter your choice (rock, paper, scissors): ").lower()
        
        if player1 not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please choose either 'rock', 'paper', or 'scissors'.")
            continue
        
        Computerbot = generate_computer_choice()
        print(f"The computer chose: {Computerbot}")
        
        winner = determine_winner(player1, Computerbot)
        
        if winner == 'player':
            player_wins += 1
            print("You win this round!")
        elif winner == 'computer':
            computer_wins += 1
            print("The computer wins this round!")
        else:
            print("It's a tie for this round!")
        
        rounds += 1
        print(f"Score after {rounds} round(s): Player {player_wins}, Computer {computer_wins}\n")
    
    if player_wins == 2:
        print("Congratulations! You've won the game.")
    else:
        print("The computer has won the game.")

# Run the game
rock_paper_scissors()
