from tkinter import *
from tkinter import ttk
from tkinter.font import Font
from tkinter import Text, Tk
from tkinter import messagebox
from tkcalendar import Calendar, DateEntry
import datetime
import os
import sys
#Click the buttons on the left side to better understand our code

#Main Calendar Page
class CalendarPage():
    def __init__(self, root):
        root.title("LBYCPA1 Project")
        root.protocol("WM_DELETE_WINDOW", lambda : sys.exit())
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

#Create Calendar Page
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

        #Putting 0s on digits with less than 2
        splitDate = date.split("-")
        if int(splitDate[0]) < 10:
            splitDate[0] = "0" + splitDate[0]
        if int(splitDate[1]) < 10:
            splitDate[1] = "0" + splitDate[1]
        splitDate[2] = "20" + splitDate[2]
        date = "-".join(splitDate)


        fileName = subject + ".txt"
        # debug
        # print(date)
        # print(subject)
        # print(task)

        #Create the folder first for the date
        try:
            os.mkdir("data\\tasks//"+date)
        except:
            pass

        #Try to open the 'date' file in tasks folder then write the txt
        try:
            with open("data\\tasks\\" + date + "\\" + fileName, mode = "x", encoding = "utf8") as text:
                text.writelines("Date: " + date + "\n" + "Subject: " + subject + "\n" + task)
            with open("data\\tasks\\_master.txt", mode = "a", encoding = "utf8") as master:
                master.write("\n" + date + ";" + fileName)
       
            with open("data\\tasks\\_master.txt", mode = "r", encoding = "utf8") as sortIT:
                lines = sortIT.readlines()
            lines[-1] = lines[-1] + "\n"
            lines = sorted(lines)
            concatenation = ""
            for line in lines:
                print(line)
                concatenation = concatenation + line
            with open("data\\tasks\\_master.txt", mode = "w", encoding = "utf8") as rewrite:
                rewrite.write(concatenation.rstrip("\n"))
        except FileExistsError:
            self.errorString.set("Subject already has task in date!! Go to edit to add/mark as done/delete tasks")
        
#Edit Calendar Page
class EditCalendar():
    def __init__(self, root):
        root.title("LBYCPA1 Project")
        root.protocol("WM_DELETE_WINDOW", lambda : exit())
        self.root = root
        optionList = self.loadList()
        #Configuring styles
        style = ttk.Style()
        style.configure('Helvetica.TButton', font=("Helvetica", 14))


        style = ttk.Style()
        style.configure('HelveticaT.TLabel', font=("Helvetica", 24, "bold"))
        style = ttk.Style()
        style.configure('Helvetica.TLabel', font=("Helvetica", 14))

        myLabel = ttk.Label(root, text="Edit", style = "HelveticaT.TLabel")
        myLabel.grid(row = 0, column = 0, columnspan = 4, padx = 50, pady = 20)

        ttk.Button(root, text = "Back", width = 16, command = self.back).grid(column = 0, row = 4, padx = 4, sticky = W, pady = 8)

        ttk.Label(root, text = "Choose: ", style = "Helvetica.TLabel").grid(row =1, column = 0, sticky = W)
        self.titleText = StringVar(root)
        self.titleText.set("Select a Date - Subject")
        OptionMenu(root, self.titleText, *optionList).grid(column = 1, row = 1, sticky = (W,N), ipadx = 120, padx = 32)
       
        ttk.Button(root, text = "Load", width = 16, command = self.loadContent).grid(column = 2, row = 1, padx = 4, sticky = E, pady = 8)
        ttk.Button(root, text = "Save", width = 16, command = self.saveContent).grid(column = 2, row = 2, padx = 4, sticky = E, pady = 8)
        ttk.Button(root, text = "Delete", width = 14, command = self.delete).grid(column = 2, row = 3, padx = 4, sticky = E, pady = 8)
        
        ttk.Label(root, text = "Tasks:", style = 'Helvetica.TLabel').grid(row = 2, column = 0, sticky = W)
        
        self.taskText = Text(root, width = 87, height = 30)
        self.taskText.grid(columnspan = 2, column = 0, row = 3, padx = 10, pady = 10, sticky = (N,W))



        #A dropdown to pick a Subject on said date DONE!
        #A load button that loads the tasks of the chosen subject on said date IN PROGRESS
        #A delete button that removes the task
        #A Mark as done button that moves the task to accomplished
        #A save button that saves the edits

    def loadContent(self, *args):
        try:
            for line in self.listText:
                if (self.titleText.get().replace(" - ",";") + ".txt") == line:
                    chosen = line.split(";")
                    self.Idate = chosen[0]
                    self.Isubj = chosen[1]
                    self.filename = ("data\\tasks\\" + self.Idate + "\\" + self.Isubj)
            with open(self.filename, mode = "r", encoding = "utf8") as text:
                textread = text.readlines()
            textread = "".join(textread[2:])
            self.taskText.delete(1.0, "end")
            self.taskText.insert(1.0, textread)
        except:
            pass

    def saveContent(self, *args):
        task = self.taskText.get("1.0",'end-1c')
        date = self.Idate
        subject = self.Isubj.strip(".txt")
        try:
            with open(self.filename, mode = "w", encoding = "utf8") as text:
                text.writelines("Date: " + date + "\n" + "Subject: " + subject + "\n" + task)
        except:
            pass
        else:
            messagebox.showinfo("Saved!", "Tasks saved!")
        finally:
            text.close()


    def loadList(self, *args):
        loadedList = []
        with open("data\\tasks\\_master.txt", mode = "r", encoding = "utf8") as text:
            self.listText = text.readlines()
        self.listText = [i.strip("\n") for i in self.listText] 
        for line in self.listText:
            if line != '':
                loadedList.append(line.replace(";"," - ").replace(".txt",""))
        return loadedList

    def delete(self, *args):
        try:
            for line in self.listText:
                if (self.titleText.get().replace(" - ",";") + ".txt") == line:
                    chosen = line.split(";")
                    self.Idate = chosen[0]
                    self.Isubj = chosen[1]
                    self.filename = ("data\\tasks\\" + self.Idate + "\\" + self.Isubj)
        except:
            pass
        os.remove(self.filename)

        with open("data\\tasks\\_master.txt", mode = "r", encoding = "utf8") as removeLine:
            lines = removeLine.readlines()
        lines[-1] = lines[-1] + "\n"
        lines = sorted(lines)
        selected = (self.Idate + ";" + self.Isubj)
        concatenation = ""
        for line in lines:
            if not selected in line:
                concatenation = concatenation + line
        with open("data\\tasks\\_master.txt", mode = "w", encoding = "utf8") as rewrite:
            rewrite.write(concatenation.rstrip("\n"))
        self.root.destroy()
        self.new_window = Tk()
        CalendarPage(self.new_window)



    def back(self, *args):
        self.root.destroy()
        self.new_window = Tk()
        CalendarPage(self.new_window)
        pass

#View Calendar Page
class ViewCalendar():
    def __init__(self, root):
        root.title("LBYCPA1 Project")
        root.protocol("WM_DELETE_WINDOW", lambda : exit())
        self.root = root
        root.update_idletasks()

        #Configuring styles
        style = ttk.Style()
        style.configure('Helvetica.TButton', font=("Helvetica", 14))

        style = ttk.Style()
        style.configure('Helvetica.TLabel', font=("Helvetica", 44, "bold"))

        myLabel = ttk.Label(root, text="View", style = "Helvetica.TLabel")
        myLabel.grid(row = 0, column = 0, columnspan = 4, padx = 50, pady = 20)

        ttk.Button(root, text = "Back", width = 16, command = self.back).grid(column = 0, row = 5, columnspan = 3, padx = 4, sticky = W, pady = 8)

        # View calendar with events (tags)
        
        cal = Calendar(root, selectmode='none')
        with open("data\\tasks\\_master.txt", mode = "r", encoding = "utf8") as removeLine:
            lines = removeLine.readlines()
        dates = []
        for line in lines:
            if not (line == '\n' or line == ''):
                dates.append(line.rstrip("\n"))
        dates = sorted(dates)

        for date in dates:
            date = date.split(";")
            dmy = date[0].split("-")
            buffer = datetime.datetime(int(dmy[2]),int(dmy[0]),int(dmy[1]))
            cal.calevent_create(buffer, date[1].rstrip(".txt"), 'reminder')

        cal.tag_config('reminder', background='red', foreground='yellow')

        cal.grid(row=1,column=0,columnspan=3,padx=10,ipadx=10)
        ttk.Label(root, text="Hover over to see deadlines.").grid(row=2,column=0,columnspan=3)


        self.taskText = Text(root, width = 87, height = 30)
        
        self.taskText.grid(columnspan = 2, column = 0, row = 3, padx = 10, pady = 10, sticky = (N,W))

        #Insert to taskText ebrything
        everything = []
        for date in dates:
            date = date.split(";")
            foldername = date[0]
            filename = date[1]
            with open("data\\tasks\\" + foldername + "\\" + filename, mode = "r", encoding = "utf8") as read:
                lines = read.readlines()
            everything.append(lines)

        for thing in everything:
            for x in thing:
                x = x.rstrip("\n")
                x = x + "\n"
                self.taskText.insert(END, x)
        self.taskText.configure(state='disabled')
            #     if (self.titleText.get().replace(" - ",";") + ".txt") == line:
            #         chosen = line.split(";")
            #         self.Idate = chosen[0]
            #         self.Isubj = chosen[1]
            #         self.filename = ("data\\tasks\\" + self.Idate + "\\" + self.Isubj)
            # with open(self.filename, mode = "r", encoding = "utf8") as text:
            #     textread = text.readlines()
            # textread = "".join(textread[2:])
            # self.taskText.delete(1.0, "end")
            # self.taskText.insert(1.0, textread)
        
    

    def back(self, *args):
        self.root.destroy()
        self.new_window = Tk()
        CalendarPage(self.new_window)
        pass