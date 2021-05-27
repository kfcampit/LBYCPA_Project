from tkinter import *
from tkinter import ttk
from tkinter.font import Font
import os

class notebookMain:
    def __init__(self, root):
        self.root = root
        root.title("LBYCPA1 Project")
        root.protocol("WM_DELETE_WINDOW", lambda: exit())

        mainframe = Frame(root)
        mainframe.grid(column = 0, row = 0, padx = 4, pady = 8)

        Label(mainframe, text = "Notes", font = Font(family = "Helvetica", size = 14, weight = "bold")).grid(columnspan = 3, column = 1, row = 1, pady = 4)

        ttk.Button(mainframe, text = "View", command = self.gotoNotebookView, width = 16).grid(column = 1, row = 2, pady = 4, padx = 8)
        ttk.Button(mainframe, text = "Create", command = self.gotoNotebookCreate, width = 16).grid(column = 2, row = 2, pady = 4, padx = 8)
        ttk.Button(mainframe, text = "Back", width = 16, command = self.back).grid(column = 3, row = 2, pady = 4, padx = 8)

        root.mainloop()

    def gotoNotebookView(self, *args):
        self.root.destroy()
        self.new_window = Tk()
        notebookView(self.new_window)
        pass

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

        Label(mainframe, text = "Create Note", font = Font(family = "Helvetica", size = 16, weight = "bold")).grid(columnspan = 2, column = 1, row = 1, pady = 4, sticky = (W, E))

        ttk.Label(mainframe, text = "Title:", font = Font(family = "Helvetica", size = 12)).grid(column = 1, row = 2, sticky = W)

        self.titleText = StringVar()
        ttk.Entry(mainframe, textvariable = self.titleText, width = 100).grid(column = 2, row = 2, padx = 4, sticky = W)

        ttk.Label(mainframe, text = "Content:", font = Font(family = "Helvetica", size = 12)).grid(column = 1, row = 3, sticky = W)
        
        self.contentText = Text(mainframe, width = 96, height = 26)
        self.contentText.grid(columnspan = 2, column = 1, row = 4, padx = 4)

        self.errorString = StringVar()
        self.textError = ttk.Label(mainframe, textvariable = self.errorString)
        self.textError.grid(columnspan = 2, column = 1, sticky = (E, W))

        ttk.Button(mainframe, text = "Save", width = 16, command = self.save).grid(column = 2, row = 5, padx = 4, sticky = E, pady = 8)
        ttk.Button(mainframe, text = "Back", width = 16, command = self.back).grid(column = 1, row = 5, padx = 4, sticky = W, pady = 8)

    def save(self, *args):
        content = self.contentText.get("1.0",'end-1c')
        fileName = self.titleText.get().lower().replace(" ", "_") + ".txt"
        try:
            assert fileName != ".txt" and self.titleText.get() != ""

            with open("data\\notes\\" + fileName, mode = "x", encoding = "utf8") as text:
                text.writelines(self.titleText.get() + "\n" + content)
            with open("data\\notes\\_master.txt", mode = "a", encoding = "utf8") as master:
                master.write("\n" + fileName + ";" + self.titleText.get())
            self.root.destroy()
            self.new_window = Tk()
            notebookMain(self.new_window)
        except FileExistsError:
            self.errorString.set("Filename is in Use!")
        except AssertionError:
            self.errorString.set("Please add a title!")
        
    def back(self, *args):
        self.root.destroy()
        self.new_window = Tk()
        notebookMain(self.new_window)

class notebookView:
    def __init__(self, root):
        self.root = root
        root.title("LBYCPA1 Project")
        root.geometry("800x620+64+64")

        root.protocol("WM_DELETE_WINDOW", lambda: exit())
        mainframe = Frame(root)
        mainframe.grid(column = 0, row = 0, padx = 8, pady = 8)

        Label(mainframe, text = "Create Note", font = Font(family = "Helvetica", size = 16, weight = "bold")).grid(columnspan = 2, column = 1, row = 1, pady = 4, sticky = (W, E))

        ttk.Label(mainframe, text = "Title:", font = Font(family = "Helvetica", size = 12)).grid(column = 1, row = 2, sticky = W, pady = 8)
        ttk.Button(mainframe, text = "Load", width = 16, command = self.loadContent).grid(column = 2, row = 2, padx = 4, sticky = E, pady = 8)
        ttk.Button(mainframe, text = "Delete", width = 16, command = self.delete).grid(column = 2, row = 3, padx = 4, sticky = E, pady = 4)

        self.titleText = StringVar(root)
        self.titleText.set("Select a Notebook")
        optionList = self.loadList()

        OptionMenu(root, self.titleText, *optionList).grid(column = 0, row = 0, sticky = (W, N), ipadx = 120, pady = 50, padx = 64)
        ttk.Label(mainframe, text = "Content:", font = Font(family = "Helvetica", size = 12)).grid(column = 1, row = 4, sticky = W)
        
        self.contentText = Text(mainframe, width = 96, height = 26)
        self.contentText.grid(columnspan = 2, column = 1, row = 5, padx = 4)

        self.errorString = StringVar()
        self.textError = ttk.Label(mainframe, textvariable = self.errorString)
        self.textError.grid(columnspan = 2, column = 1, sticky = (E, W))

        ttk.Button(mainframe, text = "Save", width = 16, command = self.save).grid(column = 2, row = 6, padx = 4, sticky = E, pady = 8)
        ttk.Button(mainframe, text = "Back", width = 16, command = self.back).grid(column = 1, row = 6, padx = 4, sticky = W, pady = 8)

    def loadList(self, *args):
        loadedList = []

        with open("data\\notes\\_master.txt", mode = "r", encoding = "utf8") as text:
            self.listText = text.readlines()
        for line in self.listText:
            loadedList.append(line.split(";")[1][:-1])
        return loadedList

    def loadContent(self, *args):
        try:
            for line in self.listText:
                if self.titleText.get() == line.split(";")[1][:-1]:
                    self.fileName = line.split(";")[0]
            with open("data\\notes\\" + self.fileName, mode = "r", encoding = "utf8") as text:
                title = text.readline()
                content = "".join(text.readlines())
            self.contentText.delete(1.0, "end")
            self.contentText.insert(1.0, content)
        except:
            pass

    def delete(self, *args):
        if self.titleText.get() != "Select a Notebook":
            for line in self.listText:
                if self.titleText.get() == line.split(";")[1][:-1]:
                    self.fileName = line.split(";")[0]
        os.remove("data\\notes\\" + self.fileName)

        with open("data\\notes\\_master.txt", mode = "r", encoding = "utf8") as removeLine:
            lines = removeLine.readlines()
        with open("data\\notes\\_master.txt", mode = "w", encoding = "utf8") as rewrite:
            for line in lines:
                if not self.fileName in line:
                    rewrite.write(line[:-1] + "\n")

        self.root.destroy()
        self.new_window = Tk()
        notebookMain(self.new_window)

    def save(self, *args):
        with open("data\\notes\\" + self.fileName, mode = "w", encoding = "utf8") as text:
                text.writelines(self.titleText.get() + "\n" + self.contentText.get("1.0",'end-1c'))

        
        self.root.destroy()
        self.new_window = Tk()
        notebookMain(self.new_window)
    
    def back(self, *args):
        self.root.destroy()
        self.new_window = Tk()
        notebookMain(self.new_window)
