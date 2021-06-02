from schedulePage import *
from notebook import notebookMain
from gradeCalculator import gradeCalculator
from CalendarPage import CalendarPage
from flashcards import *
from tkinter import *
from tkinter import ttk
from tkinter.font import Font
import sys


class mainMenu:
    def __init__(self, root):
        self.root = root
        root.title("LBYCPA1 Project")
        root.geometry("400x400+64+64")
        mainframe = Frame(root)
        #Create the Labels and the Buttons
        ttk.Label(mainframe, text = "Virtual Sudent\nPlanner", font = Font(family = 'Corbel', size = 20, weight = "bold"), justify = 'center')
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

    #The functions of each command
    def enlistPage(self, *args):
        self.root.destroy()
        self.new_window = Tk()
        enlistMain(self.new_window)
        pass

    def calendarPage(self, *args):
        self.root.destroy()
        self.new_window = Tk()
        CalendarPage(self.new_window)
        pass

    def schedulePage(self, *args):
        self.root.destroy()
        self.new_window = Tk()
        schedulePage(self.new_window)
        pass

    def gradesPage(self, *args):
        self.root.destroy()
        self.new_window = Tk()
        gradeCalculator(self.new_window)
        pass

    def flashcardsPage(self, *args):
        self.root.destroy()
        self.new_window = Tk()
        flashcard(self.new_window)
        pass

    def notesPage(self, *args):
        self.root.destroy()
        self.new_window = Tk()
        notebookMain(self.new_window)
        pass

    def exitProgram(self, *args):
        sys.exit(0)