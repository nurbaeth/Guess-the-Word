import random

class GuessTheWordGame:
    def __init__(self):
        self.words = ['python', 'java', 'ruby', 'javascript', 'swift']
        self.word_to_guess = random.choice(self.words)
        self.guessed_word = ['_'] * len(self.word_to_guess)
        self.attempts = 6
        self.incorrect_guesses = []

    def display_word(self):
        print("Word to guess:", " ".join(self.guessed_word))
        print(f"Incorrect guesses: {', '.join(self.incorrect_guesses)}")
        print(f"Remaining attempts: {self.attempts}")

    def guess_letter(self, letter):
        if letter in self.word_to_guess:
            for i, char in enumerate(self.word_to_guess):
                if char == letter:
                    self.guessed_word[i] = letter
            print(f"Good guess! '{letter}' is in the word.")
        else:
            self.incorrect_guesses.append(letter)
            self.attempts -= 1
            print(f"Sorry, '{letter}' is not in the word.")
        
    def is_game_over(self):
        if self.attempts <= 0:
            print("Game Over! You've run out of attempts.")
            return True
        if '_' not in self.guessed_word:
            print("Congratulations! You've guessed the word!")
            return True
        return False

    def play(self):
        print("Welcome to 'Guess the Word'!")
        while not self.is_game_over():
            self.display_word()
            guess = input("Guess a letter: ").lower()
            if len(guess) == 1 and guess.isalpha():
                self.guess_letter(guess)
            else:
                print("Invalid input. Please enter a single letter.")
        print(f"The word was: {self.word_to_guess}")


if __name__ == "__main__":
    game = GuessTheWordGame()
    game.play()
