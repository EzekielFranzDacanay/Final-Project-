quiz_data = [
    {"question": "Which planet is closest to the Sun?", "options": ["A) Mercury", "B) Venus", "C) Earth", "D) Mars"], "answer": "A"},
    {"question": "Who wrote 'The Catcher in the Rye'?", "options": ["A) J.D. Salinger", "B) Ernest Hemingway", "C) F. Scott Fitzgerald", "D) Mark Twain"], "answer": "A"},
    {"question": "What is the largest organ in the human body?", "options": ["A) Liver", "B) Skin", "C) Heart", "D) Lungs"], "answer": "B"},
    {"question": "What is the deepest part of the ocean?", "options": ["A) Marianas Trench", "B) Puerto Rico Trench", "C) Java Trench", "D) Tonga Trench"], "answer": "A"},
    {"question": "Who painted 'The Starry Night'?", "options": ["A) Vincent van Gogh", "B) Pablo Picasso", "C) Leonardo da Vinci", "D) Claude Monet"], "answer": "A"},
    {"question": "What is the largest desert in the world?", "options": ["A) Sahara", "B) Gobi", "C) Antarctic", "D) Kalahari"], "answer": "A"},
    {"question": "Who invented the telephone?", "options": ["A) Alexander Graham Bell", "B) Thomas Edison", "C) Nikola Tesla", "D) Guglielmo Marconi"], "answer": "A"},
    {"question": "What is the tallest mountain in the world?", "options": ["A) Mount Everest", "B) K2", "C) Kangchenjunga", "D) Lhotse"], "answer": "A"},
    {"question": "What is the largest mammal on Earth?", "options": ["A) Blue Whale", "B) African Elephant", "C) Giraffe", "D) Hippopotamus"], "answer": "A"},
    {"question": "What is the main ingredient in hummus?", "options": ["A) Chickpeas", "B) Lentils", "C) Black Beans", "D) Kidney Beans"], "answer": "A"},
    {"question": "Who is the author of 'War and Peace'?", "options": ["A) Leo Tolstoy", "B) Fyodor Dostoevsky", "C) Anton Chekhov", "D) Ivan Turgenev"], "answer": "A"},
    {"question": "What is the chemical symbol for gold?", "options": ["A) Ag", "B) Au", "C) Pt", "D) Fe"], "answer": "B"},
    {"question": "What is the largest continent by land area?", "options": ["A) Asia", "B) Africa", "C) North America", "D) Europe"], "answer": "A"},
    {"question": "Who discovered penicillin?", "options": ["A) Alexander Fleming", "B) Marie Curie", "C) Louis Pasteur", "D) Robert Koch"], "answer": "A"},
    {"question": "What is the chemical formula for water?", "options": ["A) H2O", "B) CO2", "C) O2", "D) NaCl"], "answer": "A"},
    {"question": "What is the smallest planet in our solar system?", "options": ["A) Mercury", "B) Mars", "C) Venus", "D) Pluto"], "answer": "A"},
    {"question": "Who wrote '1984'?", "options": ["A) George Orwell", "B) Aldous Huxley", "C) Ray Bradbury", "D) H.G. Wells"], "answer": "A"},
    {"question": "What is the largest moon of Saturn?", "options": ["A) Titan", "B) Enceladus", "C) Mimas", "D) Iapetus"], "answer": "A"},
    {"question": "What is the largest artery in the human body?", "options": ["A) Aorta", "B) Pulmonary Artery", "C) Carotid Artery", "D) Femoral Artery"], "answer": "A"},
    {"question": "Who painted 'The Last Supper'?", "options": ["A) Leonardo da Vinci", "B) Michelangelo", "C) Raphael", "D) Donatello"], "answer": "A"},
    {"question": "What is the largest bird in the world by wingspan?", "options": ["A) Wandering Albatross", "B) Andean Condor", "C) Dalmatian Pelican", "D) Great Bustard"], "answer": "A"},
    {"question": "What is the main ingredient in traditional paella?", "options": ["A) Rice", "B) Couscous", "C) Quinoa", "D) Bulgur"], "answer": "A"},
    {"question": "What is the currency of Brazil?", "options": ["A) Real", "B) Peso", "C) Rupee", "D) Yen"], "answer": "A"},
    {"question": "Who was the first American President?", "options": ["A) George Washington", "B) Thomas Jefferson", "C) Abraham Lincoln", "D) John Adams"], "answer": "A"},
    {"question": "What is the national flower of Japan?", "options": ["A) Sakura (Cherry Blossom)", "B) Chrysanthemum", "C) Orchid", "D) Lily"], "answer": "A"},
    {"question": "What is the main ingredient in traditional borscht?", "options": ["A) Beetroot", "B) Tomatoes", "C) Carrots", "D) Potatoes"], "answer": "A"},
    {"question": "What is the chemical symbol for potassium?", "options": ["A) K", "B) P", "C) Ko", "D) Pn"], "answer": "A"},
    {"question": "What is the national animal of Australia?", "options": ["A) Kangaroo", "B) Koala", "C) Emu", "D) Platypus"], "answer": "A"},
    {"question": "What is the main ingredient in traditional falafel?", "options": ["A) Chickpeas", "B) Lentils", "C) Black Beans", "D) Kidney Beans"], "answer": "A"},
    {"question": "Who is the author of 'To Kill a Mockingbird'?", "options": ["A) Harper Lee", "B) Truman Capote", "C) John Steinbeck", "D) William Faulkner"], "answer": "A"},
    {"question": "What is the national sport of Canada?", "options": ["A) Ice Hockey", "B) Lacrosse", "C) Curling", "D) Soccer"], "answer": "A"},
    {"question": "What is the largest island in the world?", "options": ["A) Greenland", "B) New Guinea", "C) Borneo", "D) Madagascar"], "answer": "A"},
    {"question": "Who wrote 'The Old Man and the Sea'?", "options": ["A) Ernest Hemingway", "B) F. Scott Fitzgerald", "C) Mark Twain", "D) Jack London"], "answer": "A"},
    {"question": "What is the capital of Russia?", "options": ["A) Moscow", "B) Saint Petersburg", "C) Novosibirsk", "D) Yekaterinburg"], "answer": "A"},
    {"question": "What is the largest moon of Jupiter?", "options": ["A) Ganymede", "B) Europa", "C) Callisto", "D) Io"], "answer": "A"},
]

def ask_question(question_data, question_number):
    print(f"Question {question_number + 1}: {question_data['question']}")
    for option in question_data['options']:
        print(option)
    answer = input("Your answer (A, B, C, or D): ").strip().upper()
    while answer not in ["A", "B", "C", "D"]:
        print("Invalid input. Please enter A, B, C, or D.")
        answer = input("Your answer (A, B, C, or D): ").strip().upper()
    return answer


def run_quiz(quiz_data):
    user_answers = []
    correct_count = 0

    for i, question_data in enumerate(quiz_data):
        user_answer = ask_question(question_data, i)
        correct = user_answer == question_data['answer']
        user_answers.append((i, user_answer, correct))
        if correct:
            correct_count += 1

    print("\nQuiz Completed!")
    print(f"You answered {correct_count} out of {len(quiz_data)} questions correctly.")

    return user_answers


def review_answers(quiz_data, user_answers):
    print("\nReview your answers:")
    for i, user_answer, correct in user_answers:
        question_data = quiz_data[i]
        print(f"Question {i + 1}: {question_data['question']}")
        print(f"Your answer: {user_answer} {'(Correct)' if correct else '(Incorrect)'}
