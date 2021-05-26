from tkinter import *
from tkinter import ttk
from tkinter.font import Font

class notebookMain:
    def __init__(self, root):
        self.root = root
        root.title("LBYCPA1 Project")
        root.protocol("WM_DELETE_WINDOW", lambda: exit())

        mainframe = Frame(root)
        mainframe.grid(column = 0, row = 0, padx = 4, pady = 8)

        Label(mainframe, text = "Schedules", font = Font(family = "Helvetica", size = 14, weight = "bold")).grid(columnspan = 3, column = 1, row = 1, pady = 4)

        Button(mainframe, text = "View & Edit Schedule", command = self.notebookPopUp, width = 16).grid(column = 1, row = 2, pady = 4, padx = 8)
        Button(mainframe, text = "Add Sched", command = self.gotoNotebookCreate, width = 16).grid(column = 2, row = 2, pady = 4, padx = 8)
        Button(mainframe, text = "Back", width = 16, command = self.back).grid(column = 3, row = 2, pady = 4, padx = 8)

        root.mainloop()

    def notebookPopUp (self):
        root = Toplevel()
        root.title("LBYCPA1 Project")

        root.geometry("600x200")

        canvasOne = Canvas(root)
        frameOne = Frame(canvasOne)
        Label(frameOne, text="hello")

        canvas = Canvas(root)
        scroll_y = Scrollbar(root, orient = "vertical", command=canvas.yview)

        frame = Frame(canvas)
        
        with open("data\\notes\\scheduleinventory.txt", mode = "r", encoding = "utf8") as text:
            textNames = text.readlines()
            formatNames = [i[:-1] for i in textNames[:-1]]
            formatNames.append(textNames[-1])

        for i, fileName in enumerate(formatNames):
            Label(frame, text = fileName.split(";")[1], width = 48, justify = "left").grid(column = 0, row = i, padx = 8, pady = 8)
            Button(frame, text = "Edit", width = 12).grid(column = 4, row = i, padx = 4)
            Button(frame, text = "Delete", width = 12).grid(column = 5, row = i, padx = 4)

        canvas.create_window(0, 0, anchor='nw', window=frame)

        canvas.update_idletasks()

        canvas.configure(scrollregion=canvas.bbox('all'), yscrollcommand=scroll_y.set)
                        
        canvas.pack(fill='both', expand=True, side='left')
        scroll_y.pack(fill='y', side='right')


    def gotoNotebookCreate(self, *args):
        self.root.destroy()
        self.new_window = Tk()
        notebookCreate(self.new_window)

    def back(self, *args):
        self.root.destroy()
        pass

class notebookCreate:
    def __init__(self, root):
        self.root = root
        root.title("LBYCPA1 Project")
        root.geometry("800x600+64+64")

        root.protocol("WM_DELETE_WINDOW", lambda: exit())
        mainframe = Frame(root)
        mainframe.grid(column = 0, row = 0, padx = 8, pady = 8)

        Label(mainframe, text = "Create Schedule", font = Font(family = "Helvetica", size = 16, weight = "bold")).grid(columnspan = 2, column = 1, row = 1, pady = 4, sticky = (W, E))

        Label(mainframe, text = "Title:", font = Font(family = "Helvetica", size = 12)).grid(column = 1, row = 2, sticky = W)

        self.titleText = StringVar()
        Entry(mainframe, textvariable = self.titleText, width = 100).grid(column = 2, row = 2, padx = 4, sticky = W)

        Label(mainframe, text = "Time:", font = Font(family = "Helvetica", size = 12)).grid(column = 1, row = 3, sticky = W)
        
        self.contentText = Text(mainframe, width = 96, height = 26)
        self.contentText.grid(columnspan = 2, column = 1, row = 4, padx = 4)

        Button(mainframe, text = "Save", width = 16, command = self.save).grid(column = 2, row = 5, padx = 4, sticky = E, pady = 8)
        Button(mainframe, text = "Back", width = 16, command = self.back).grid(column = 1, row = 5, padx = 4, sticky = W, pady = 8)

    def save(self, *args):
        content = self.contentText.get("1.0",'end-1c')
        fileName = self.titleText.get().lower().replace(" ", "_") + ".txt"
        with open("data\\notes\\" + fileName, mode = "x", encoding = "utf8") as text:
            text.writelines(self.titleText.get() + "\n" + content)
        with open("data\\notes\\scheduleinventory.txt", mode = "a", encoding = "utf8") as inventory:
            inventory.write("\n" + fileName + ";" + self.titleText.get())
        self.back

    def back(self, *args):
        self.root.destroy()
        self.new_window = Tk()
        notebookMain(self.new_window)

class notebookEdit:
    def __init__(self, root):
        self.root = root
        root.title("LBYCPA1 Project")

root = Tk()
notebookMain(root)