import random
from config import *
import PySimpleGUI as gui

class HangmanGame:
    def __init__(self, config: GameConfiguration = None):
        self.config =  GameConfiguration()
        self.artist = HangmanArtist()
        self.validator = GuessValidator()
        self.reset_game()

    def reset_game(self) -> None:
        self.word = random.choice(self.config.word_list).lower()
        self.guessed_letters: Set[str] = set()
        self.remaining_attempts = self.config.max_attempts
        self.status = GameStatus.IN_PROGRESS
        self.display = WordDisplay(self.word, self.guessed_letters)
    
    def process_guess(self, guess: str) -> str:
        if self.status != GameStatus.IN_PROGRESS:
            return f"Game is over! The word was {self.word}. Start a new game!"
        guess = guess.lower()
        is_valid, error_message = self.validator.validate_guess(guess, self.guessed_letters)
        if not is_valid:
            return error_message
        self.guessed_letters.add(guess)
        return self._evaluate_guess(guess)

    def _evaluate_guess(self, guess: str) -> str:
        if guess not in self.word:
            self.remaining_attempts -= 1
            if self.remaining_attempts == 0:
                self.status = GameStatus.LOST
                return f"Game Over! The word was {self.word}"
            return f"Wrong guess! {self.remaining_attempts} attempts left"
        if self.display.is_word_completed():
            self.status = GameStatus.WON
            return f"Congratulations! You won! The word was {self.word}"
        return "Good guess!"

    def get_game_display(self) -> str:
        return (
            f"{self.artist.get_hangman_state(self.remaining_attempts)}\n"
            f"\nWord: {self.display.get_display_state()}"
            f"\nGuessed letters: {', '.join(sorted(self.guessed_letters)) or 'None'}"
            f"\nRemaining attempts: {self.remaining_attempts}"
        )

    