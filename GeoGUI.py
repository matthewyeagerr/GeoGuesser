from tkinter import *
import csv
import random

# Load capitals data from file
def load_capitals(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)

# --- GUI version of the game ---
class GeoGame:
    def __init__(self, master, data):
        self.master = master
        self.data = data
        self.index = 0
        self.score = 0
        self.streak = 0

        master.title("GeoGuessr Lite - Capital Edition")
        master.geometry("500x350")
        
        for widget in master.winfo_children():
            widget.destroy()
        self.show_start_screen()
        
        
    def show_start_screen(self):
        label = Label(self.master, text = "Select number of questions:", font=("Arial", 16))
        label.pack(pady=20)
        
        for num in range(10,51,10):
            button = Button(self.master, text=f"{num} Questions", command=lambda n=num: self.start_game(n))
            button.pack(pady=5)
            
    def start_game(self, num_questions):
        self.num_questions = num_questions
        self.index = 0
        self.score = 0
        self.streak = 0
        self.data = random.sample(self.data, k=min(num_questions, len(self.data)))
        
        for widget in self.master.winfo_children():
            widget.destroy()

        self.capital_label = Label(self.master, text="", font=("Arial", 16))
        self.capital_label.pack(pady=20)

        self.entry = Entry(self.master, font=("Arial", 14))
        self.entry.pack()

        self.feedback_label = Label(self.master, text="", font=("Arial", 12))
        self.feedback_label.pack(pady=10)

        self.score_label = Label(self.master, text="Score: 0 | Streak: 0", font=("Arial", 12))
        self.score_label.pack(pady=5)

        self.submit_button = Button(self.master, text="Submit Guess", command=self.check_answer)
        self.submit_button.pack(pady=10)

        self.hint_button = Button(self.master, text="Hint (?)", command=self.show_hint)
        self.hint_button.pack()

        self.next_question()

    def next_question(self):
        if self.index >= len(self.data):
            self.capital_label.config(text="🏁 Game Over!")
            self.feedback_label.config(text=f"Final Score: {self.score}/{len(self.data)} ({(self.score/len(self.data))*100:.2f}%)")
            self.entry.config(state=DISABLED)
            self.submit_button.config(state=DISABLED)
            self.hint_button.config(state=DISABLED)
            return

        self.current = self.data[self.index]
        self.capital_label.config(text=f"{self.index+1}. What country has the capital '{self.current['Capital']}'?")
        self.entry.delete(0, END)
        self.feedback_label.config(text="")

    def check_answer(self):
        guess = self.entry.get().strip()
        if guess.lower() == self.current['Country'].lower():
            self.score += 1
            self.streak += 1
            self.feedback_label.config(text="✅ Correct!", fg="green")
        else:
            self.feedback_label.config(text=f"❌ Wrong. It was {self.current['Country']}", fg="red")
            self.streak = 0

        self.index += 1
        self.score_label.config(text=f"Score: {self.score} | Streak: {self.streak}")
        self.master.after(1000, self.next_question)  # wait 1 second, then show next

    def show_hint(self):
        cap = self.current['Capital']
        self.feedback_label.config(
            text=f"Hint: Capital starts with '{cap[0]}', {len(cap)} letters.",
            fg="blue"
        )

# Run the app
if __name__ == "__main__":
    data = load_capitals("Capitals.txt")

    root = Tk()
    game = GeoGame(root, data)
    root.mainloop()
