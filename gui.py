import PySimpleGUI as gui
from engine import *

class GUIInterface:
    """Handles the PySimpleGUI interface"""
    def __init__(self):
        self.game = HangmanGame()
        self.theme = gui.theme('DarkGrey13')
        self.window = self.create_window()

    def create_window(self):
        """Creates the main game window"""
        layout = [
            [gui.Text('Welcome to Hangman!', font=('Helvetica', 20))],
            [gui.Multiline(self.game.get_game_display(), size=(50, 15), key='-DISPLAY-', 
                         font=('Courier New', 12), disabled=True)],
            [gui.Text('Enter your guess:', font=('Helvetica', 12))],
            [gui.Input(size=(5, 1), key='-GUESS-', font=('Helvetica', 12)),
             gui.Button('Submit', bind_return_key=True)],
            [gui.Text('', size=(40, 1), key='-MESSAGE-', font=('Helvetica', 12))],
            [gui.Button('New Game'), gui.Button('Exit')]
        ]
        return gui.Window('Hangman Game', layout, finalize=True)

    def play(self):
        """Main game loop"""
        while True:
            event, values = self.window.read()

            if event in (gui.WIN_CLOSED, 'Exit'):
                break

            if event == 'New Game':
                self.game.reset_game()
                self.window['-MESSAGE-'].update('')
                self.window['-GUESS-'].update('')

            if event == 'Submit':
                guess = values['-GUESS-'].strip()
                if guess:
                    result = self.game.process_guess(guess)
                    self.window['-MESSAGE-'].update(result)
                    self.window['-GUESS-'].update('')
                    
                    if self.game.status != GameStatus.IN_PROGRESS:
                        if gui.popup_yes_no('Would you like to play again?') == 'Yes':
                            self.game.reset_game()
                            self.window['-MESSAGE-'].update('')
                        else:
                            break

            # Update the display after each action
            self.window['-DISPLAY-'].update(self.game.get_game_display())

        self.window.close()

if __name__ == "__main__":
    gui_interface = GUIInterface()
    gui_interface.play()
