from enlist import enlistMain
from tkinter import *
from tkinter import ttk
from tkinter.font import Font

from numpy import delete

class schedulePage:
    def __init__(self, root):
        self.root = root
        root.title("LBYCPA1 Project")
        root.protocol("WM_DELETE_WINDOW", lambda: exit())

        mainframe = Frame(root)
        mainframe.grid(column = 0, row = 0, padx = 8, pady = 8)

        calendar = Frame(mainframe, background = "green3")
        calendar.grid(columnspan = 2, column = 1, row = 2, padx = 8, pady = 8)

        Label(mainframe, text = "Schedule", font = Font(family = "Helvetica", size = 14, weight = "bold")).grid(columnspan = 2, column = 1, row = 1, pady = 4)

        self.initializeSchedule()

        days = ["TIME", "MONDAY", "TEUSDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY"]
        
        for d, day in enumerate(days):
            Label(calendar, text = day, width = 16, borderwidth = 1, relief = "groove", background = "green4").grid(column = d, row = 0, sticky = (W, E))

        for time, t in enumerate(range(1, ((self.lateTime - self.earlyTime) * 2) + 1, 2), self.earlyTime):
            Label(calendar, text = str(time) + ":00", width = 16, height = 2, borderwidth = 1, relief = "groove", background = "green3").grid(rowspan = 2, column = 0, row = t, sticky = (W, E))

        self.labelColors = [["PaleGreen1" for x in range(1, 7)] for y in range(1, ((self.lateTime - self.earlyTime) * 2) + 1)]
        self.labelText = [["" for x in range(1, 7)] for y in range(1, ((self.lateTime - self.earlyTime) * 2) + 1)]
        self.loadColors()

        for i in range(1, ((self.lateTime - self.earlyTime) * 2) + 1):
            for j in range(1, 7):
               Label(calendar, width = 16, text = self.labelText[i - 1][j - 1], height = 1, borderwidth = 1, relief = "groove", background = self.labelColors[i - 1][j - 1]).grid(column = j, row = i, sticky = (W, E))

        self.titleText = StringVar(root)
        self.titleText.set("Select a Course")
        self.optionList = [n[0] for n in self.classTimes]

        OptionMenu(mainframe, self.titleText, *self.optionList).grid(column = 1, row = 3, ipadx = 90, sticky = E)
        ttk.Button(mainframe, text = "Delete", width = 16, command = self.delete).grid(column = 2, row = 3, sticky = W, padx = 4, pady = 4)

        ttk.Button(mainframe, text = "Enlist", width = 16, command = self.gotoEnlist).grid(column = 1, row = 4, sticky = W, padx = 4, pady = 4)
        ttk.Button(mainframe, text = "Back", width = 16, command = self.back).grid(column = 2, row = 4, sticky = E, padx = 4, pady = 4)


        


        
    def loadColors(self):
        colors = ["red", "blue", "yellow", "orange", "snow"]
        c = 0

        for classInfo in self.classTimes:
            for day in classInfo[-3]:
                if day == "M": d = 0
                elif day == "T": d = 1
                elif day == "W": d = 2
                elif day == "H": d = 3
                elif day == "F": d = 4
                elif day == "S": d = 5

                n = (int(classInfo[-2]) // 100) - self.earlyTime
                n *= 2
                if int(classInfo[-2]) % 100 >= 30:
                    n += 1
        
                m = (int(classInfo[-1]) // 100) - self.earlyTime
                m *= 2
                if int(classInfo[-1]) % 100 >= 30:
                    m += 1
                
                for i in range(n, m):
                    self.labelColors[i][d] = colors[c]

                self.labelText[n][d] = classInfo[0]
            c += 1

    def initializeSchedule(self):
        with open("data\\schedule\\sched.txt", mode = "r", encoding = "utf8") as readSched:
            holder = readSched.readlines()
        self.classSched = [classData.strip().split(";") for classData in holder]

        times = []

        for item in self.classSched:
            times.append(int(float(item[-2])))
            times.append(int(float(item[-1])))
        
        self.earlyTime = min(times) // 100
        self.lateTime = max(times) // 100
        
        self.classTimes = [[i[0], i[-3], int(float(i[-2])), int(float(i[-1])) ] for i in self.classSched]
        pass

    def delete(self, *args):
        with open("data\\schedule\\sched.txt", mode = "r", encoding = "utf8") as removeLine:
            lines = removeLine.readlines()
        with open("data\\schedule\\sched.txt", mode = "w", encoding = "utf8") as rewrite:
            for line in lines:
                if not self.titleText.get() in line:
                    rewrite.write(line[:-1] + "\n")

        self.root.destroy()
        self.new_window = Tk()
        schedulePage(self.new_window)

    def gotoEnlist(self):
        self.root.destroy()
        self.new_window = Tk()
        enlistMain(self.new_window)
    
    def back(self, *args):
        self.root.destroy()
        pass


root = Tk()
schedulePage(root)
root.mainloop()