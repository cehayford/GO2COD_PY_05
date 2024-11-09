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

    