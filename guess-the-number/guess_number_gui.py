import tkinter as tinker
from guess_number import guessNumber

class GuessNumber:
    
    def __init__(self):
        self.main_window = tinker.Tk()

    def run_application(self):
        self.main_window.mainloop()


if __name__ == '__main__':
    window = GuessNumber()
    window.run_application()