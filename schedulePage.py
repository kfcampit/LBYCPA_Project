from tkinter import *
from tkinter import ttk
from tkinter.font import Font
import pandas as pd
import os

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

        days = ["TIME", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY"]
        
        for d, day in enumerate(days):
            Label(calendar, text = day, width = 16, borderwidth = 1, relief = "groove", background = "green4").grid(column = d, row = 0, sticky = (W, E))

        for time, t in enumerate(range(1, ((self.lateTime - self.earlyTime) * 2) + 3, 2), self.earlyTime):
            Label(calendar, text = str(time) + ":00", width = 16, height = 2, borderwidth = 1, relief = "groove", background = "green3").grid(rowspan = 2, column = 0, row = t, sticky = (W, E))

        self.labelColors = [["PaleGreen1" for x in range(1, 7)] for y in range(1, ((self.lateTime - self.earlyTime) * 2) + 3)]
        self.labelText = [["" for x in range(1, 7)] for y in range(1, ((self.lateTime - self.earlyTime) * 2) + 3)]

        try:
            self.loadColors()
        except:
            pass

        for i in range(1, ((self.lateTime - self.earlyTime) * 2) + 3):
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
        colors = ["red", "blue", "yellow", "orange", "snow", "purple1", "VioletRed1", "goldenrod1", "snow4", "dark olive green", "light cyan", "colar"]
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


#I ADDED THIS HERE so i can go back and forth
class enlistMain:
    def __init__(self, root):
        self.root = root
        root.title("LBYCPA1 Project")
        root.geometry("320x480+64+64")

        root.protocol("WM_DELETE_WINDOW", lambda: exit())
        mainframe = Frame(root)
        mainframe.grid(column = 0, row = 0, padx = 8, pady = 8)

        Label(mainframe, text = "Enlistment", font = Font(family = "Helvetica", size = 16, weight = "bold")).grid(columnspan = 2, column = 1, row = 1, pady = 4, sticky = (W, E))
        ttk.Separator(mainframe, orient = HORIZONTAL).grid(columnspan = 2, column = 1, row = 2, ipadx = 140, pady = 16)

        Label(mainframe, text = "Search Courses", font = Font(family = "Helvetica", size = 12, weight = "bold")).grid(columnspan = 2, column = 1, row = 3, pady = 4, sticky = (W, E))
        Label(mainframe, text = "Enter course code", font = Font(family = "Helvetica", size = 8, slant = "italic")).grid(columnspan = 2, column = 1, row = 4, pady = 4, sticky = (W, E))
        
        self.courseCode = StringVar()
        ttk.Entry(mainframe, textvariable = self.courseCode, width = 24).grid(column = 1, row = 5, padx = 2, sticky = W)
        ttk.Button(mainframe, text = "Search", command = self.coursePopup, width = 16).grid(column = 2, row = 5, sticky = E)

        ttk.Separator(mainframe, orient = HORIZONTAL).grid(columnspan = 2, column = 1, row = 6, ipadx = 140, pady = 16)
        Label(mainframe, text = "Add Courses", font = Font(family = "Helvetica", size = 12, weight = "bold")).grid(columnspan = 2, column = 1, row = 7, pady = 4, sticky = (W, E))
        Label(mainframe, text = "Enter course number", font = Font(family = "Helvetica", size = 8, slant = "italic")).grid(columnspan = 2, column = 1, row = 8, pady = 4, sticky = (W, E))

        self.courseNo = StringVar()
        ttk.Entry(mainframe, textvariable = self.courseNo, width = 24).grid(column = 1, row = 9, padx = 2, sticky = W)
        ttk.Button(mainframe, text = "Check", command = self.getData, width = 16).grid(column = 2, row = 9, pady = 8, sticky = E)

        self.courseName = StringVar()
        Label(mainframe, textvariable = self.courseName, width = 32, font = Font(size = 12, family =  "Helvetica"), borderwidth = 1, relief = "groove").grid(columnspan = 2, column = 1, row = 10, sticky = (W, E))
        
        self.facultyName = StringVar()
        Label(mainframe, textvariable = self.facultyName, width = 32, font = Font(size = 12, family =  "Helvetica"), borderwidth = 1, relief = "groove").grid(columnspan = 2, column = 1, row = 11, sticky = (W, E))

        self.courseCde = StringVar()
        Label(mainframe, textvariable = self.courseCde, width = 16, font = Font(size = 12, family =  "Helvetica"), borderwidth = 1, relief = "groove").grid(column = 1, row = 12, sticky = (W, E))

        self.section = StringVar()
        Label(mainframe, textvariable = self.section, width = 16, font = Font(size = 12, family =  "Helvetica"), borderwidth = 1, relief = "groove").grid(column = 2, row = 12, sticky = (W, E))
        
        self.day = StringVar()
        Label(mainframe, textvariable = self.day, width = 16, font = Font(size = 12, family =  "Helvetica"), borderwidth = 1, relief = "groove").grid(column = 1, row = 13, sticky = (W, E))

        self.time = StringVar()
        Label(mainframe, textvariable = self.time, width = 16, font = Font(size = 12, family =  "Helvetica"), borderwidth = 1, relief = "groove").grid(column = 2, row = 13, sticky = (W, E))

        self.errorText = StringVar()
        Label(mainframe, textvariable = self.errorText, font = Font(family = "Helvetica", size = 8, slant = "italic")).grid(column = 1, row = 14, sticky = W, pady = 8)
        self.saveButton = ttk.Button(mainframe, text = "Save", width = 16, command = self.save)
        ttk.Button(mainframe, text = "View Calendar", width = 20, command = self.gotoSchedule).grid(column = 2, row = 15, sticky = E, pady = 4)
        ttk.Button(mainframe, text = "Back", width = 16, command = self.back).grid(column = 1, row = 15, padx = 4, sticky = W, pady = 4)
        
        self.courseName.set("Course Name")
        self.facultyName.set("Professor Name")
        self.courseCde.set("Course Code")
        self.section.set("Section")
        self.day.set("Day")
        self.time.set("Start time - End time")



    def coursePopup(self):
        root = Toplevel()
        root.title("LBYCPA1 Project")
        root.geometry("1100x200")

        canvas = Canvas(root)
        scroll_y = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)

        self.read = pd.read_csv('data\\database\\gcoe_t2_2021_database.csv')
        data = self.read.loc[self.read["COURSE CODE"] == self.courseCode.get(), ["CLASS NO", "COURSE CODE", "COURSE TITLE", "OFFERED to", "SEC", "FACULTY", "DAY1", "BEGIN1", "END1"]]
        self.result = []

        for index, rows in data.iterrows():
            self.result.append([str(int(rows["CLASS NO"])), rows["COURSE CODE"], rows["COURSE TITLE"], rows["OFFERED to"], rows["SEC"], rows["FACULTY"], rows["DAY1"], str(int(rows["BEGIN1"])), str(int(rows["END1"]))])

        frame = Frame(canvas)

        Label(frame, text = "NO.", width = 8, justify = "left", font = Font(size = 12, family =  "Helvetica"), borderwidth = 1, relief = "ridge", bg = "grey").grid(column = 0, row = 0, sticky = W)
        Label(frame, text = "CODE", width = 12, justify = "left", font = Font(size = 12, family =  "Helvetica"), borderwidth = 1, relief = "ridge", bg = "grey").grid(column = 1, row = 0, sticky = W)
        Label(frame, text = "COURSE TITLE", justify = "left", font = Font(size = 12, family =  "Helvetica"), borderwidth = 1, relief = "ridge", width = 32, bg = "grey").grid(column = 2, row = 0, sticky = W)
        Label(frame, text = "SEC", justify = "left", font = Font(size = 12, family =  "Helvetica"), borderwidth = 1, relief = "ridge", width = 8, bg = "grey").grid(column = 3, row = 0, sticky = W)
        Label(frame, text = "FACULTY", justify = "left", font = Font(size = 12, family =  "Helvetica"), borderwidth = 1, relief = "ridge", width = 32, bg = "grey").grid(column = 4, row = 0, sticky = W)
        Label(frame, text = "DAY", justify = "left", font = Font(size = 12, family =  "Helvetica"), borderwidth = 1, relief = "ridge", width = 8, bg = "grey").grid(column = 5, row = 0, sticky = W)
        Label(frame, text = "TIME", justify = "left", font = Font(size = 12, family =  "Helvetica"), borderwidth = 1, relief = "ridge", width = 16, bg = "grey").grid(column = 6, row = 0, sticky = W)

        for i in range(len(self.result)):
            Label(frame, text = self.result[i][0], width = 8, justify = "left", font = Font(size = 12, family =  "Helvetica"), borderwidth = 1, relief = "ridge").grid(column = 0, row = i + 1, sticky = W)
            Label(frame, text = self.result[i][1], width = 12, justify = "left", font = Font(size = 12, family =  "Helvetica"), borderwidth = 1, relief = "ridge").grid(column = 1, row = i + 1, sticky = W)
            Label(frame, text = self.result[i][2], justify = "left", font = Font(size = 12, family =  "Helvetica"), borderwidth = 1, relief = "ridge", width = 32).grid(column = 2, row = i + 1, sticky = W)
            Label(frame, text = (self.result[i][3] + self.result[i][4]), justify = "left", font = Font(size = 12, family =  "Helvetica"), borderwidth = 1, relief = "ridge", width = 8).grid(column = 3, row = i + 1, sticky = W)
            Label(frame, text = self.result[i][5], justify = "left", font = Font(size = 12, family =  "Helvetica"), borderwidth = 1, relief = "ridge", width = 32).grid(column = 4, row = i + 1, sticky = W)
            Label(frame, text = self.result[i][6], justify = "left", font = Font(size = 12, family =  "Helvetica"), borderwidth = 1, relief = "ridge", width = 8).grid(column = 5, row = i + 1, sticky = W)
            Label(frame, text = (self.result[i][7] + " - " + self.result[i][8]), justify = "left", font = Font(size = 12, family =  "Helvetica"), borderwidth = 1, relief = "ridge", width = 16).grid(column = 6, row = i + 1, sticky = W)

        canvas.create_window(0, 0, anchor='nw', window=frame)

        canvas.update_idletasks()

        canvas.configure(scrollregion=canvas.bbox('all'), yscrollcommand=scroll_y.set)
                        
        canvas.pack(fill='both', expand=True, side='left')
        scroll_y.pack(fill='y', side='right')

    def getData(self):
        self.read = pd.read_csv('data\\database\\gcoe_t2_2021_database.csv')
        searched = self.read.loc[self.read["CLASS NO"] == int(self.courseNo.get()), ["COURSE CODE", "COURSE TITLE", "OFFERED to", "SEC", "FACULTY", "DAY1", "BEGIN1", "END1"]]
        self.resultDetails = searched.values.tolist()[0]

        self.courseName.set(self.resultDetails[1])
        self.facultyName.set(self.resultDetails[4])
        self.courseCde.set(self.resultDetails[0])
        self.section.set(self.resultDetails[2] + self.resultDetails[3])
        self.day.set(self.resultDetails[5])
        self.time.set(str(int(self.resultDetails[6])) + " - " + str(int(self.resultDetails[7])))

        self.saveButton.grid(column = 2, row = 14, padx = 4, sticky = E, pady = 8)

    def checkValidity(self, x, y):
        startC, endC, startS, endS = float(x[-2]), float(x[-1]), float(y[-2]), float(y[-1])
        if not ((startC >= startS and endC <= endS) or (startC <= startS and endC >= endS) or (startS <= startC <= endS or startC <= endC <= endS)):
            return True
        return False

    def save(self, *args):
        checkList = self.resultDetails
        if os.stat("data\\schedule\\sched.txt").st_size == 0:
            with open("data\\schedule\\sched.txt", mode = "a", encoding = "utf8") as writeText:
                writeText.write(";".join(list(map(str, checkList))))
        else:
            if len(checkList[5]) == 2:
                checkList[5] = [checkList[5][0], checkList[5][1]]

            with open("data\\schedule\\sched.txt", mode = "r", encoding = "utf8") as schedText:
                storedSched = [line.strip().split(";") for line in schedText.readlines()]
            for line in storedSched:
                if len(line[5]) == 2:
                    line[5] = [line[5][0], line[5][1]]
            valid = []

            #StoredSched = sched exisiting

            for classSched in storedSched:
                #Case 1, if the input has same day (2 days) with the previous schedules and the subject names are different
                if len(checkList[5]) == 2 and (checkList[5][0] in classSched[5] or checkList[5][1] in classSched[5]) and checkList[0] != classSched[0]:
                    valid.append(self.checkValidity(checkList, classSched))
                    
                #Case 2, if the input has same day (1 day) with the previous schedules and the subject names are different
                elif len(checkList[5]) == 1 and checkList[5] in classSched[5] and checkList[0] != classSched[0]:
                    valid.append(self.checkValidity(checkList, classSched))
                    

                #Case 3, if the input has no same day with the previous schedules and the subject names are different
                elif checkList[0] != classSched[0]:
                    valid.append(True)
                    
                #If not in cases
                else:
                    valid.append(False)
                    
            if all(valid):
                with open("data\\schedule\\sched.txt", mode = "a", encoding = "utf8") as writeText:
                    if len(checkList[5]) == 2:
                        checkList[5] = checkList[5][0] + checkList[5][1]
                    addschedule =  ";".join(list(map(str, checkList))).rstrip("\n")
                    writeText.write(str(addschedule) + "\n")
                self.errorText.set("")
            else:
                self.errorText.set("Invalid schedule")
        
    def gotoSchedule(self):
        self.root.destroy()
        self.new_window = Tk()
        schedulePage(self.new_window)

    def back(self, *args):
        self.root.destroy()

# root = Tk()
# schedulePage(root)
# root.mainloop()