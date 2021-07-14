import tkinter as tinker
from guess_number import guessNumber

class GuessNumber:
    
    def __init__(self):
        self.main_window = tinker.Tk()
        self.main_window.title('Guess The Number')
        self.main_window.geometry('500x500')
        self.create_widgets(self.main_window)

    def create_widgets(self,master):
        self.menu = tinker.Menu(master=master)
        self.file_menu = tinker.Menu(self.menu, tearoff=0)
        self.file_menu.add_command(label='Exit',command= master.quit)
        master.config(menu=self.menu)

    def run_application(self):
        self.main_window.mainloop()


if __name__ == '__main__':
    window = GuessNumber()
    window.run_application()