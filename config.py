from dataclasses import dataclass
from enum import Enum
from typing import Set, List

class GameStatus(Enum):
    IN_PROGRESS = "in_progress"
    WON = "won"
    LOST = "lost"

@dataclass
class GameConfiguration:
    max_attempts: int = 6
    word_list: List[str] = None

    def __post_init__(self):
        if self.word_list is None:
            self.word_list = [
                "python", "programming", "computer", "algorithm", "database",
                "network", "software", "developer", "internet", "security"
            ]

class WordDisplay:
    def __init__(self, word: str, guessed_letters: Set[str]):
        self.word = word
        self.guessed_letters = guessed_letters

    def get_display_state(self) -> str:
        return " ".join(
            letter if letter in self.guessed_letters else "_"
            for letter in self.word
        )

    def is_word_completed(self) -> bool: 
        return all(letter in self.guessed_letters for letter in self.word)

class HangmanArtist:
    def get_hangman_state(self, remaining_attempts: int) -> str:
        stages = [
            # stages 0-6 remain the same as in original code
            """
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |     / \\
               -
            """,
            """
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |     /
               -
            """,
            """
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |
               -
            """,
            """
               --------
               |      |
               |      O
               |     \\|
               |      |
               |
               -
            """,
            """
               --------
               |      |
               |      O
               |      |
               |      |
               |
               -
            """,
            """
               --------
               |      |
               |      O
               |
               |
               |
               -
            """,
            """
               --------
               |      |
               |
               |
               |
               |
               -
            """
        ]
        return stages[remaining_attempts]

class GuessValidator:
    @staticmethod
    def validate_guess(guess: str, guessed_letters: Set[str]) -> tuple[bool, str]:
        if not guess.isalpha() or len(guess) != 1:
            return False, "Please enter a single letter!"
        if guess in guessed_letters:
            return False, f"You already guessed '{guess}'!"
        
        return True, ""