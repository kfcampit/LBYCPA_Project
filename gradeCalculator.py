from tkinter import *
from tkinter import ttk
from tkinter.font import Font

class calculate:
    def __init__(self, root):
        root.title("LBYCPA1 Project")

        mainframe = ttk.Frame(master = root, padding="4 8 12 12", width = 400, height = 400)
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        self.gradeInput = StringVar()
        gradeEntry = ttk.Entry(mainframe, width = 32, textvariable = self.gradeInput)
        gradeEntry.grid(column = 2, columnspan = 2, row = 3, sticky = (E), pady = 4, padx = 8)

        self.percentInput = StringVar()
        percentEntry = ttk.Entry(mainframe, width = 32, textvariable = self.percentInput)
        percentEntry.grid(column = 2, columnspan = 2, row = 4, sticky = (E),  pady = 8, padx = 8)

        self.grade = StringVar()
        ttk.Label(mainframe, textvariable = self.grade).grid(row = 5, sticky = (W, E))
        ttk.Button(mainframe, text = "Calculate", command = self.getGrade).grid(column = 3, row = 6, sticky = E)
        ttk.Button(mainframe, text = "Back", command = self.back).grid(column = 1, row = 6, sticky = W)

        ttk.Label(mainframe, text = "Grade Calculator", font = Font(family = 'Helvetica', size = 12, weight = "bold")).grid(column = 2, row = 1, sticky = (E), pady = 8)
        ttk.Label(mainframe, text = "intructions", font = Font(size = 8, slant = "italic")).grid(column = 2, row = 2, sticky = (E))

        ttk.Label(mainframe, text = "Scores:").grid(column = 1, row = 3, sticky = W)
        ttk.Label(mainframe, text = "Percentage:").grid(column = 1, row = 4, sticky = W)

    def getGrade(self, *args):
        try:
            pass
        except ValueError:
            pass

    def back(self, *args):
            pass

root = Tk()
calculate(root)
root.mainloop()