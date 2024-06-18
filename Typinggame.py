import time

def calculate_accuracy(original_text, typed_text):
    """Calculates accuracy of typed text compared to original."""
    original_length = len(original_text)
    typed_length = len(typed_text)
    
    if original_length == 0 or typed_length == 0:
        return 0.0
    
    correct_count = sum(1 for i in range(min(original_length, typed_length)) if original_text[i] == typed_text[i])
    accuracy = (correct_count / original_length) * 100
    return accuracy

def typing_challenge(text):
    """Displays text to the user and challenges them to type it."""
    print("Type the following text:")
    print(text)
    
    input("Press Enter when you are ready to start typing...")
    start_time = time.time()
    typed_text = input("Start typing: ")
    end_time = time.time()
    
    typing_time = end_time - start_time
    accuracy = calculate_accuracy(text, typed_text)
    
    print(f"\nTime taken: {typing_time:.2f} seconds")
    print(f"Accuracy: {accuracy:.2f}%")

def main():
    text = "The quick brown fox jumps over the lazy dog."
    typing_challenge(text)

if __name__ == "__main__":
    main()
