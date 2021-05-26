from tkinter import *
from tkinter import ttk
from tkinter.font import Font
from tkinter import Text, Tk
from tkinter import messagebox
from tkcalendar import Calendar, DateEntry



class CalendarPage():
    def __init__(self, root):
        root.title("LBYCPA1 Project")
        root.protocol("WM_DELETE_WINDOW", lambda : exit())
        self.root = root

        #Configuring styles
        style = ttk.Style()
        style.configure('Helvetica.TButton', font=("Helvetica", 14))

        style = ttk.Style()
        style.configure('Helvetica.TLabel', font=("Helvetica", 44, "bold"))

        myLabel = ttk.Label(root, text="CALENDAR", style = "Helvetica.TLabel")
        myLabel.grid(row = 0, column = 0, columnspan = 4, padx = 50, pady = 20)

        ttk.Button(root, text = "Back", command = self.back, style = 'Helvetica.TButton').grid(column = 3, row = 2, padx = 8, pady = 10)

        ttk.Button(root, text = "Create", command = self.create, style = 'Helvetica.TButton').grid(column = 0, row = 2, padx = 8, pady = 10)

        ttk.Button(root, text = "Edit", command = self.back, style = 'Helvetica.TButton').grid(column = 1, row = 2, padx = 8, pady = 10)

        ttk.Button(root, text = "View", command = self.back, style = 'Helvetica.TButton').grid(column = 2, row = 2, padx = 8, pady = 10)

    #Program Functions
    def create(self, *args):
        self.root.destroy()
        self.new_window = Tk()
        CreateCalendar(self.new_window)
        pass




    def back(self, *args):
        self.root.destroy()
        pass


class CreateCalendar():
    def __init__(self, root):
        root.title("LBYCPA1 Project")
        root.protocol("WM_DELETE_WINDOW", lambda : exit())
        self.root = root

        #Configuring styles
        style = ttk.Style()
        style.configure('Helvetica.TButton', font=("Helvetica", 12))

        style = ttk.Style()
        style.configure('Helvetica.TLabel', font=("Helvetica", 12))

        ttk.Label(root, text="Choose date", style = 'Helvetica.TLabel').grid(row = 1, column = 0, pady=10, sticky=W)


        global cal
        cal = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2)
        cal.grid(row = 1, column = 1, padx=4, pady=10, sticky = W)


        ttk.Label(root, text = "Subject:", style = 'Helvetica.TLabel').grid(row = 2, column = 0, sticky = W)

        self.subjectText = StringVar()
        ttk.Entry(root, textvariable = self.subjectText, width = 100).grid(row = 2, column = 1, padx = 4, sticky = W)

        ttk.Label(root, text = "Task:", style = 'Helvetica.TLabel').grid(row = 3, column = 0, sticky = W)
        
        self.taskText = Text(root, width = 87, height = 3)
        self.taskText.grid(columnspan = 2, column = 0, row = 4, padx = 4)

        #idk wat dis is
        self.errorString = StringVar()
        self.textError = ttk.Label(root, textvariable = self.errorString)
        self.textError.grid(columnspan = 2, column = 0, sticky = (E, W))

        ttk.Button(root, text = "Save", width = 16, command = self.save).grid(column = 2, row = 5, padx = 4, sticky = E, pady = 8)
        ttk.Button(root, text = "Back", width = 16, command = self.back).grid(column = 1, row = 5, padx = 4, sticky = W, pady = 8)


    def back(self, *args):
        self.root.destroy()
        self.new_window = Tk()
        CalendarPage(self.new_window)
        pass

    def save(self, *args):
        global cal
        print("AYAW GUMANAA")
        date = str(cal.get_date())
        print(cal.get_date())

