from tkinter import *
from tkinter import ttk
from tkinter.font import Font
import pandas as pd
import os

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
            for classSched in storedSched:
                if len(checkList[5]) == 2 and (checkList[5][0] in classSched[5] or checkList[5][1] in classSched[5]) and checkList[0] != classSched[0]:
                    valid.append(self.checkValidity(checkList, classSched))
                elif len(checkList[5]) == 1 and checkList[5] in classSched[5] and checkList[0] != classSched[0]:
                    valid.append(self.checkValidity(checkList, classSched))
                else:
                    valid.append(False)
            if all(valid):
                with open("data\\schedule\\sched.txt", mode = "a", encoding = "utf8") as writeText:
                    if len(checkList[5]) == 2:
                        checkList[5] = checkList[5][0] + checkList[5][1]
                    writeText.write("\n" + ";".join(list(map(str, checkList))))
                self.errorText.set("")
            else:
                self.errorText.set("Invalid schedule")
        
    def gotoSchedule(self):
        self.root.destroy()
        self.new_window = Tk()
        schedulePage(self.new_window)

    def back(self, *args):
        self.root.destroy()