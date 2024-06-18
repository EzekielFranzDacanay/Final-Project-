import random

def number_guessing_game():
    target_number = random.randint(1, 100)
    attempts = 0
    
    print("Hello, Welcome to Number Guessing Game, try your luck!")
    print("try and guess up to 1-100!")
    
    while True:
        player = input("Enter your guess: ")
        
        if not player.isdigit():
            print("Please enter a valid number.")
            continue
        
        player = int(player)
        attempts += 1
        
        if player < target_number:
            print("Too low! Try again.")
        elif player > target_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {target_number} correctly in {attempts} attempts.")
            break

number_guessing_game()
