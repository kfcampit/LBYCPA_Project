from tkinter import *
from tkinter import ttk
from tkinter.font import Font
import pandas as pd

class enlistMain:
    def __init__(self, root):
        self.root = root
        root.title("LBYCPA1 Project")
        root.geometry("800x600+64+64")

        root.protocol("WM_DELETE_WINDOW", lambda: exit())
        mainframe = Frame(root)
        mainframe.grid(column = 0, row = 0, padx = 8, pady = 8)

        Label(mainframe, text = "Create Note", font = Font(family = "Helvetica", size = 16, weight = "bold")).grid(columnspan = 2, column = 1, row = 1, pady = 4, sticky = (W, E))
        
        self.courseCode = StringVar()
        ttk.Entry(mainframe, textvariable = self.courseCode, width = 40).grid(column = 1, row = 2, padx = 8, sticky = W)
        Button(mainframe, text = "Search", command = self.coursePopup).grid(column = 2, row = 2)
        
        
        
    def coursePopup(self):
        root = Toplevel()
        root.title("LBYCPA1 Project")

        canvas = Canvas(root)
        scroll_y = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)

        self.read = pd.read_csv('data\\database\\gcoe_t2_2021_database.csv')
        data = self.read.loc[self.read["COURSE CODE"] == self.courseCode.get(), ["CLASS NO", "COURSE CODE", "COURSE TITLE", "SEC"]]
        self.result = []

        for index, rows in data.iterrows():
            self.result.append(" | ".join([str(int(rows["CLASS NO"])), rows["COURSE CODE"], rows["COURSE TITLE"], rows["SEC"]]))

        frame = Frame(canvas)
        for i in range(len(self.result)):
            Label(frame, text = self.result[i], width = 48, justify = "left", font = Font(size = 12, family =  "Helvetica"), borderwidth = 1, relief = "ridge").grid(column = 0, row = i, sticky = W)
        canvas.create_window(0, 0, anchor='nw', window=frame)

        canvas.update_idletasks()

        canvas.configure(scrollregion=canvas.bbox('all'), yscrollcommand=scroll_y.set)
                        
        canvas.pack(fill='both', expand=True, side='left')
        scroll_y.pack(fill='y', side='right')




root = Tk()
enlistMain(root)
root.mainloop()