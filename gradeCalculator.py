from tkinter import *
from tkinter import ttk
from tkinter.font import Font

class gradeCalculator():
    def __init__(self, root):
        root.title("LBYCPA1 Project")
        self.root = root

        self.instructionText = "Input your scores with \'/\' and with each being seperated by a space. Input your percentages as decimals (ex. 0.25). Ensure same amount of elements for both."

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

        self.gradeOutput = StringVar()
        ttk.Label(mainframe, textvariable = self.gradeOutput, font = Font(size = 10)).grid(column = 2, row = 5, sticky = (W), pady = 10, padx = 4)
        ttk.Button(mainframe, text = "Calculate", command = self.getGrade).grid(column = 3, row = 6, sticky = E)

        ttk.Button(mainframe, text = "Back", command = self.back).grid(column = 1, row = 6, sticky = W, padx = 8)

        ttk.Label(mainframe, text = "Grade Calculator", font = Font(family = 'Helvetica', size = 12, weight = "bold")).grid(column = 2, row = 1, sticky = (E), pady = 8)
        ttk.Label(mainframe, text = self.instructionText, font = Font(size = 8, slant = "italic"), wraplength = 300, justify = "center").grid(pady = 8 ,columnspan = 4, column = 0, row = 2, sticky = (E, W))

        ttk.Label(mainframe, text = "Scores:").grid(column = 1, row = 3, sticky = W, padx = 4)
        ttk.Label(mainframe, text = "Percentage:").grid(column = 1, row = 4, sticky = W, padx = 4)
        ttk.Label(mainframe, text = "Grade:", font = Font(weight = "bold", size = 10)).grid(column = 1, row = 5, sticky = E, pady = 8)
        
        gradeEntry.focus()
        percentEntry.focus()

        root.bind("<Return>", self.getGrade)


    #Program Functions
    
    def getGrade(self, *args):
        try:
            #Compute for grade
            stringScores = str(self.gradeInput.get())
            stringPercentages = str(self.percentInput.get())
            listScore = stringScores.split()
            listPercentages = list(map(float ,stringPercentages.split()))
            listFloatScores = [(int(i.split("/")[0])) / int((i.split("/")[1])) for i in listScore]

            assert len(listScore) == len(listPercentages)
            assert sum(listPercentages) == 1

            grade = round(sum([(a * b) for a, b in zip(listFloatScores, listPercentages)]) * 100, 2)

            self.gradeOutput.set(str(grade) + "%")
        except:
            self.gradeOutput.set("Wrong Format!")

    def back(self, *args):
        self.root.destroy()
        pass