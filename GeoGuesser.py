import csv
import random



# Load data from CSV
def load_capitals(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)


    

# Ask user to guess
def play_game(data, num_questions=50):
    print("🌍 Welcome to 'Guess the Country by Capital'! You'll get 50 capitals and have to name the country it resides in! Try to get above 75%! Good Luck!")
    print("Type the correct country for the given capital.\n")

    score = 0
    streak = 0
    questions = random.sample(data, k=min(num_questions, len(data)))
    

    for i, entry in enumerate(questions, start=1):
        capital = entry['Capital']
        country = entry['Country']
        
        
        while True:

            guess = input(f"{i}. What country has the capital '{capital}'? \n")
        
            if guess =="?":
                print(f"The capital starts with the letter '{capital[0]}'.\nThe capital also has {len(capital)} letters.\n")
                
            else:
                break
            

        if guess.lower() == country.lower():
            print("✅ Correct!\n")
            score += 1
            streak+= 1
            print(f"Current streak: {streak}\n")

        else: 
            print(f"❌ Wrong. The correct answer was: {country}\n")
            streak = 0

    print(f"🏁 Game Over! Your score: {score}/{num_questions}")
    accuracy = (score / num_questions) * 100
    print(f"Your accuracy: {accuracy:.2f}%\n")

if __name__ == "__main__":
    data = load_capitals("Capitals.txt")
    play_game(data)
