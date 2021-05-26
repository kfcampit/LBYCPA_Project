from tkinter import *
from tkinter import ttk
from tkinter.font import Font
from tkinter import Text, Tk
from tkinter import messagebox
from tkcalendar import Calendar, DateEntry
import os



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

        ttk.Button(root, text = "Edit", command = self.edit, style = 'Helvetica.TButton').grid(column = 1, row = 2, padx = 8, pady = 10)

        ttk.Button(root, text = "View", command = self.view, style = 'Helvetica.TButton').grid(column = 2, row = 2, padx = 8, pady = 10)

    #Program Functions
    def create(self, *args):
        self.root.destroy()
        self.new_window = Tk()
        CreateCalendar(self.new_window)
        pass

    def view(self, *args):
        self.root.destroy()
        self.new_window = Tk()
        ViewCalendar(self.new_window)
        pass

    def edit(self, *args):
        self.root.destroy()
        self.new_window = Tk()
        EditCalendar(self.new_window)
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
        # cal = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2)
        # cal.grid(row = 1, column = 1, padx=4, pady=10, sticky = W)
        
        cal = Calendar(root, selectmode = "day", expand = "True")
        cal.grid(row = 1, column = 1, padx = 4, pady=10)


        ttk.Label(root, text = "Subject:", style = 'Helvetica.TLabel').grid(row = 2, column = 0, sticky = W)

        self.subjectText = StringVar()
        ttk.Entry(root, textvariable = self.subjectText, width = 100).grid(row = 2, column = 1, padx = 4, sticky = W)

        ttk.Label(root, text = "Tasks:", style = 'Helvetica.TLabel').grid(row = 3, column = 0, sticky = W)
        
        self.taskText = Text(root, width = 87, height = 3)
        self.taskText.grid(columnspan = 2, column = 0, row = 4, padx = 4)

        #idk wat dis is
        self.errorString = StringVar()
        self.textError = ttk.Label(root, textvariable = self.errorString)
        self.textError.grid(columnspan = 2, column = 0, sticky = (E, W))

        ttk.Button(root, text = "Save", width = 16, command = self.save).grid(column = 2, row = 6, padx = 4, sticky = E, pady = 8)
        ttk.Button(root, text = "Back", width = 16, command = self.back).grid(column = 1, row = 6, padx = 4, sticky = W, pady = 8)


    def back(self, *args):
        self.root.destroy()
        self.new_window = Tk()
        CalendarPage(self.new_window)
        pass


    #should save the inputs
    def save(self, *args):
        global cal
        self.errorString.set("")
        date = str(cal.get_date()).replace("/","-")
        subject = self.subjectText.get()
        task = self.taskText.get("1.0",'end-1c')

        fileName = subject + ".txt"
        # debug
        # print(date)
        # print(subject)
        # print(task)

        #Create the folder first for the date
        try:
            os.mkdir("data\\tasks//"+date)
        except:
            #if it doesnt work, do nothing lmao
            x = 1+1

        #Try to open the 'date' file in tasks folder then write the txt
        try:
            with open("data\\tasks\\" + date + "\\" + fileName, mode = "x", encoding = "utf8") as text:
                text.writelines("Date: " + date + "\n" + "Subject: " + subject + "\n" + task)
            with open("data\\tasks\\_master.txt", mode = "a", encoding = "utf8") as master:
                master.write("\n" + date + ";" + fileName)
       

        except FileExistsError:
            self.errorString.set("Subject already has task in date!! Go to edit to add/mark as done/delete tasks")
        




#Should show a dropdown menu of previous inputs
#Load
#Mark as Accomplished (Delete, but save on accomplish txt)
#Delete
class EditCalendar():
    def __init__(self, root):
        root.title("LBYCPA1 Project")
        root.protocol("WM_DELETE_WINDOW", lambda : exit())
        self.root = root

        #Configuring styles
        style = ttk.Style()
        style.configure('Helvetica.TButton', font=("Helvetica", 14))

        style = ttk.Style()
        style.configure('Helvetica.TLabel', font=("Helvetica", 44, "bold"))

        myLabel = ttk.Label(root, text="Edit", style = "Helvetica.TLabel")
        myLabel.grid(row = 0, column = 0, columnspan = 4, padx = 50, pady = 20)

        ttk.Button(root, text = "Back", width = 16, command = self.back).grid(column = 1, row = 5, padx = 4, sticky = W, pady = 8)


    def back(self, *args):
        self.root.destroy()
        self.new_window = Tk()
        CalendarPage(self.new_window)
        pass



#Should read the inputs
#View Calendar (above)
#View To-do list (below)
#A button to view accomplished
class ViewCalendar():
    def __init__(self, root):
        root.title("LBYCPA1 Project")
        root.protocol("WM_DELETE_WINDOW", lambda : exit())
        self.root = root

        #Configuring styles
        style = ttk.Style()
        style.configure('Helvetica.TButton', font=("Helvetica", 14))

        style = ttk.Style()
        style.configure('Helvetica.TLabel', font=("Helvetica", 44, "bold"))

        myLabel = ttk.Label(root, text="View", style = "Helvetica.TLabel")
        myLabel.grid(row = 0, column = 0, columnspan = 4, padx = 50, pady = 20)

        ttk.Button(root, text = "Back", width = 16, command = self.back).grid(column = 1, row = 5, padx = 4, sticky = W, pady = 8)


    def back(self, *args):
        self.root.destroy()
        self.new_window = Tk()
        CalendarPage(self.new_window)
        pass