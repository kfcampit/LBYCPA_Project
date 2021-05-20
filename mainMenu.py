from gradeCalculator import gradeCalculator
from tkinter import *
from tkinter import ttk
from tkinter.font import Font

class mainMenu:
    def __init__(self, root):
        self.root = root
        root.title("LBYCPA1 Project")
        root.geometry("400x400")
        mainframe = Frame(root)

        ttk.Label(mainframe, text = "Main Menu", font = Font(family = 'Helvetica', size = 16, weight = "bold"))

        ttk.Button(mainframe, text = "Enlist", command = self.enlistPage)
        ttk.Button(mainframe, text = "Calendar", command = self.calendarPage)
        ttk.Button(mainframe, text = "Schedule", command = self.schedulePage)
        ttk.Button(mainframe, text = "Grades", command = self.gradesPage)
        ttk.Button(mainframe, text = "Flashcards", command = self.flashcardsPage)
        ttk.Button(mainframe, text = "Notes", command = self.notesPage)
        ttk.Button(mainframe, text = "Exit", command = self.exitProgram)

        for child in mainframe.winfo_children():
            child.pack(fill = "x", pady = 8)

        mainframe.pack(expand = 1)

    def enlistPage(self, *args):
        
        pass

    def calendarPage(self, *args):
        pass

    def schedulePage(self, *args):
        pass

    def gradesPage(self, *args):
        self.root.destroy()
        self.new_window = Tk()
        gradeCalculator(self.new_window)
        pass

    def flashcardsPage(self, *args):
        pass

    def notesPage(self, *args):
        pass

    def exitProgram(self, *args):
        exit()