from tkinter import *
from tkinter import ttk
from tkinter.font import Font
from tkinter import Text, Tk



class flashcard():
    def __init__(self, root):
        root.title("LBYCPA1 Project")
        self.root = root

        #Configuring styles
        style = ttk.Style()
        style.configure('Comic.TButton', font=("Comic Sans MS", 14))

        style = ttk.Style()
        style.configure('Comic.TLabel', font=("Comic Sans MS", 44, "bold"))

        myLabel = ttk.Label(root, text="FLASHCARD", style = "Comic.TLabel")
        myLabel.grid(row = 0, column = 0, columnspan = 3, padx = 50, pady = 20)

        ttk.Button(root, text = "Back", command = self.back, style = 'Comic.TButton').grid(column = 2, row = 2, padx = 8)

        createbtn = ttk.Button(root, text ="CREATE", command = self.create, style = 'Comic.TButton')
        createbtn.grid(row=1,column=0,padx=50)

        editbtn = ttk.Button(root, text ="EDIT", command = self.create, style = 'Comic.TButton')
        editbtn.grid(row = 1, column = 1, padx = 50, pady = 50)
      
        studybtn = ttk.Button(root, text ="STUDY", command = self.create, style = 'Comic.TButton')
        studybtn.grid(row = 1, column = 2, padx = 50)

    #Program Functions
    def create(self, *args):
        self.root.destroy()
        self.new_window = Tk()
        create(self.new_window)
        pass


    def back(self, *args):
        self.root.destroy()
        pass

class create():
    def __init__(self, root):
        root.title("LBYCPA1 Project")
        self.root = root
        ttk.Button(root, text = "Back", command = self.back).grid(column = 3, row = 3, padx = 30,sticky = E)

        style = ttk.Style()
        style.configure('Comic.TLabel', font=("Comic Sans MS", 14, "bold"))

        myLabel = ttk.Label(root, text= "CREATE", style = "Comic.TLabel")
        myLabel.grid(row = 0, column = 2, padx = 50, pady = 20)

        QLabel = ttk.Label(root, text= "Question", style = "Comic.TLabel")
        QLabel.grid(row = 1, column = 0, padx = 50, pady = 20)

        Question = Text(root,height = 10,width = 50)
        Question.grid(row = 2,column = 0, padx = 30, pady=30)

        ALabel = ttk.Label(root, text= "Answer", style = "Comic.TLabel")
        ALabel.grid(row = 1, column = 3, padx = 50, pady = 20)
        Answer = Text(root, height = 10, width = 50)
        Answer.grid(row = 2, column = 3, padx = 30, pady=30)

        ttk.Button(root, text = "Save", command = self.back).grid(column = 3, row = 3, padx = 30,sticky = E)

    def back(self, *args):
        self.root.destroy()
        pass