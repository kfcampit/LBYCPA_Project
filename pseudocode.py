#Import Gui functions
from tkinter import *
from tkinter import ttk
from tkinter.font import Font
from tkinter import messagebox
import os


class notebookMain:
    Module __init__(self, root):
        Set self.root = root
        Set root.title("LBYCPA1 Project")
        Set root.protocol("WM_DELETE_WINDOW", lambda: exit())

        Set mainframe = Frame(root)
        Show mainframe.grid(column = 0, row = 0, padx = 4, pady = 8)

        Set Label(mainframe, text = "Notes", font = Font(family = "Helvetica", size = 14, weight = "bold")).grid(columnspan = 3, column = 1, row = 1, pady = 4)

        Set ttk.Button(mainframe, text = "View", command = self.gotoNotebookView, width = 16).grid(column = 1, row = 2, pady = 4, padx = 8)
        Set ttk.Button(mainframe, text = "Create", command = self.gotoNotebookCreate, width = 16).grid(column = 2, row = 2, pady = 4, padx = 8)
        Set ttk.Button(mainframe, text = "Back", width = 16, command = self.back).grid(column = 3, row = 2, pady = 4, padx = 8)

        Perform root.mainloop()
        end module

    Module gotoNotebookView(self, *args):
        wait for error:
            Set optionList = self.loadList()
            Check assert optionList != []
            end wait for error
        if error occurs:
            Perform messagebox.showerror("No notes found","Create notes first to view them")
        if error not occur:
            Perform self.root.destroy()
            Perform self.new_window = Tk()
            Call notebookView(self.new_window)
        end module

    Module gotoNotebookCreate(self, *args):
        Perform self.root.destroy()
        Perform self.new_window = Tk()
        Call notebookCreate(self.new_window)
        end module

    Module back(self, *args):
        Perform self.root.destroy()
        pass
        end module
    

    Module loadList(self, *args):
        Declare loadedList as list

        with open("data\\notes\\_master.txt", mode = "r", encoding = "utf8") as text:
            Set self.listText = text.readlines()
        for line in self.listText:
            if line != '\n':
                Set loadedList.append(line.split(";")[1][:-1])
                end if
        return loadedList
        end module
    end class



class notebookCreate:
    Module __init__(self, root):
        Set self.root = root
        Set root.title("LBYCPA1 Project")
        Set root.geometry("800x600+64+64")

        Set root.protocol("WM_DELETE_WINDOW", lambda: exit())
        Set mainframe = Frame(root)
        Show mainframe.grid(column = 0, row = 0, padx = 8, pady = 8)

        Set Label(mainframe, text = "Create Note", font = Font(family = "Helvetica", size = 16, weight = "bold")).grid(columnspan = 2, column = 1, row = 1, pady = 4, sticky = (W, E))

        Set ttk.Label(mainframe, text = "Title:", font = Font(family = "Helvetica", size = 12)).grid(column = 1, row = 2, sticky = W)

        Set self.titleText = StringVar()
        Set ttk.Entry(mainframe, textvariable = self.titleText, width = 100).grid(column = 2, row = 2, padx = 4, sticky = W)

        Set ttk.Label(mainframe, text = "Content:", font = Font(family = "Helvetica", size = 12)).grid(column = 1, row = 3, sticky = W)
        
        Set self.contentText = Text(mainframe, width = 96, height = 26)
        Set self.contentText.grid(columnspan = 2, column = 1, row = 4, padx = 4)

        Set self.errorString = StringVar()
        Set self.textError = ttk.Label(mainframe, textvariable = self.errorString)
        Set self.textError.grid(columnspan = 2, column = 1, sticky = (E, W))

        Set ttk.Button(mainframe, text = "Save", width = 16, command = self.save).grid(column = 2, row = 5, padx = 4, sticky = E, pady = 8)
        Set ttk.Button(mainframe, text = "Back", width = 16, command = self.back).grid(column = 1, row = 5, padx = 4, sticky = W, pady = 8)
        end module

    Module save(self, *args):
        Set content = self.contentText.get("1.0",'end-1c')
        Set fileName = self.titleText.get().lower().replace(" ", "_") + ".txt"
        wait for error:
            Check assert fileName != ".txt" and self.titleText.get() != ""

            with open("data\\notes\\" + fileName, mode = "x", encoding = "utf8") as text:
                Set text.writelines(self.titleText.get() + "\n" + content)
            with open("data\\notes\\_master.txt", mode = "a", encoding = "utf8") as master:
                Perform master.write("\n" + fileName + ";" + self.titleText.get())
            Perform self.root.destroy()
            Perform self.new_window = Tk()
            Call notebookMain(self.new_window)
            end wait for error
        If FileExistsError:
            self.errorString.set("Filename is in Use!")
        If AssertionError:
            self.errorString.set("Please add a title!")
        end module
        
    Module back(self, *args):
        Perform self.root.destroy()
        Perform self.new_window = Tk()
        Perform notebookMain(self.new_window)
        end module

class notebookView:
    Module __init__(self, root):
        Set self.root = root
        Set root.title("LBYCPA1 Project")
        Set root.geometry("800x620+64+64")

        Set root.protocol("WM_DELETE_WINDOW", lambda: exit())
        Set mainframe = Frame(root)
        Show mainframe.grid(column = 0, row = 0, padx = 8, pady = 8)

        Set Label(mainframe, text = "Create Note", font = Font(family = "Helvetica", size = 16, weight = "bold")).grid(columnspan = 2, column = 1, row = 1, pady = 4, sticky = (W, E))

        Set ttk.Label(mainframe, text = "Title:", font = Font(family = "Helvetica", size = 12)).grid(column = 1, row = 2, sticky = W, pady = 8)
        Set ttk.Button(mainframe, text = "Load", width = 16, command = self.loadContent).grid(column = 2, row = 2, padx = 4, sticky = E, pady = 8)
        Set ttk.Button(mainframe, text = "Delete", width = 16, command = self.delete).grid(column = 2, row = 3, padx = 4, sticky = E, pady = 4)

        Declare self.titleText = StringVar(root)
        Set self.titleText.set("Select a Notebook")
        Set optionList = self.loadList()

        Set OptionMenu(root, self.titleText, *optionList).grid(column = 0, row = 0, sticky = (W, N), ipadx = 120, pady = 50, padx = 64)
            
        Set ttk.Label(mainframe, text = "Content:", font = Font(family = "Helvetica", size = 12)).grid(column = 1, row = 4, sticky = W)
        
        Set self.contentText = Text(mainframe, width = 96, height = 26)
        Show self.contentText.grid(columnspan = 2, column = 1, row = 5, padx = 4)

        Declare self.errorString = StringVar()
        Set self.textError = ttk.Label(mainframe, textvariable = self.errorString)
        Show self.textError.grid(columnspan = 2, column = 1, sticky = (E, W))

        Set ttk.Button(mainframe, text = "Save", width = 16, command = self.save).grid(column = 2, row = 6, padx = 4, sticky = E, pady = 8)
        Set ttk.Button(mainframe, text = "Back", width = 16, command = self.back).grid(column = 1, row = 6, padx = 4, sticky = W, pady = 8)
        end module

    Module loadList(self, *args):
        Declare loadedList as list
        with open("data\\notes\\_master.txt", mode = "r", encoding = "utf8") as text:
            Set self.listText = text.readlines()
        for line in self.listText:
            if line != '\n':
                Set loadedList.append(line.split(";")[1])
                end if
        return loadedList

    Module loadContent(self, *args):
        wait for error:
            Declare x as string
            for line in self.listText:
                if line != '\n':
                    Set x = (line.split(";")[1])
                    end if
                if self.titleText.get() == x:
                    Set self.fileName = (line.split(";")[0])
                    end if
            wait for error
        if error occurs:
            pass
        if error not occur:
            with open("data\\notes\\" + self.fileName, mode = "r", encoding = "utf8") as text:
                Set title = text.readline()
                Set content = "".join(text.readlines())
            Set self.contentText.delete(1.0, "end")
            Set self.contentText.insert(1.0, content)
        end moule


    Module delete(self, *args):
        if self.titleText.get() != "Select a Notebook":
            for line in self.listText:
                if self.titleText.get() == line.split(";")[1][:-1]:
                    Set self.fileName = line.split(";")[0]
                    end if
        os.remove("data\\notes\\" + self.fileName)

        with open("data\\notes\\_master.txt", mode = "r", encoding = "utf8") as removeLine:
            lines = removeLine.readlines()
        with open("data\\notes\\_master.txt", mode = "w", encoding = "utf8") as rewrite:
            for line in lines:
                if not self.fileName in line:
                    Set rewrite.write(line[:-1] + "\n")

        Perform self.root.destroy()
        Perform self.new_window = Tk()
        Call notebookMain(self.new_window)
        end module

    Module save(self, *args):
        with open("data\\notes\\" + self.fileName, mode = "w", encoding = "utf8") as text:
                Set text.writelines(self.titleText.get() + "\n" + self.contentText.get("1.0",'end-1c'))
        Perform self.root.destroy()
        Perform self.new_window = Tk()
        Call notebookMain(self.new_window)
        end module
    
    Module back(self, *args):
        Perform self.root.destroy()
        Perform self.new_window = Tk()
        Call notebookMain(self.new_window)
    end class