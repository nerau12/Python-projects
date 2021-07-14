import tkinter as tinker
from guess_number import guessNumber

class GuessNumber:
    
    def __init__(self):
        self.main_window = tinker.Tk()
        self.main_window.title('Guess The Number')
        self.main_window.geometry('500x500')
        self.menu = tinker.Menu(self.main_window)
        self.file_menu = tinker.Menu(self.menu, tearoff=0)
        self.file_menu.add_command(label="Exit",command= self.main_window.quit)
        self.main_window.config(menu=self.menu)

    def create_widgets(self):
        pass

    def run_application(self):
        self.main_window.mainloop()


if __name__ == '__main__':
    window = GuessNumber()
    window.run_application()