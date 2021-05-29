from tkinter import *
from tkinter import ttk
from gradeCalculator import *
from mainMenu import *

if __name__ == "__main__":
    running = True
    #Always run the code. This is because it is a GUI
    while running:
        root = Tk()
        root.protocol("WM_DELETE_WINDOW", lambda : exit())
        mainMenu(root)
        root.mainloop()
        