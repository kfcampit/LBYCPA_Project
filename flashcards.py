from tkinter import *
from tkinter import ttk
from tkinter.font import Font
from tkinter import Text, Tk
from tkinter import messagebox



class flashcard():
    def __init__(self, root):
        root.title("LBYCPA1 Project")
        root.protocol("WM_DELETE_WINDOW", lambda : exit())
        self.root = root

        #Configuring styles
        style = ttk.Style()
        style.configure('Comic.TButton', font=("Comic Sans MS", 14))

        style = ttk.Style()
        style.configure('Comic.TLabel', font=("Comic Sans MS", 44, "bold"))

        myLabel = ttk.Label(root, text="FLASHCARD", style = "Comic.TLabel")
        myLabel.grid(row = 0, column = 0, columnspan = 3, padx = 50, pady = 20)

        ttk.Button(root, text = "Back", command = self.back, style = 'Comic.TButton').grid(column = 2, row = 2, padx = 8, pady = 8)

        createbtn = ttk.Button(root, text ="CREATE", command = self.create, style = 'Comic.TButton')
        createbtn.grid(row=1,column=0,padx=50)

        editbtn = ttk.Button(root, text ="EDIT", command = self.edit, style = 'Comic.TButton')
        editbtn.grid(row = 1, column = 1, padx = 50, pady = 50)
      
        studybtn = ttk.Button(root, text ="STUDY", command = self.study, style = 'Comic.TButton')
        studybtn.grid(row = 1, column = 2, padx = 50)

    #Program Functions
    def create(self, *args):
        confirm = messagebox.askquestion("Delete current flashcard?","Creating a new flashcard will delete the current one. Are you sure?")
        if confirm == "yes":
            self.root.destroy()
            self.new_window = Tk()
            create(self.new_window)
        else:
            return
        pass

    def edit(self, *args):
        try:
            with open("data\\flashcards\\Flashcards.txt", mode="r") as r:
                lines = r.readlines()
        except:
            messagebox.showerror("Flashcards.txt not detected", "Make sure to CREATE first before editing")
        else:
            self.root.destroy()
            self.new_window = Tk()
            edit(self.new_window)
        pass

    def study(self, *args):
        try:
            with open("data\\flashcards\\Flashcards.txt", mode="r") as r:
                lines = r.readlines()
        except:
            messagebox.showerror("Flashcards.txt not detected", "Make sure to CREATE first before editing")
        else:
            self.root.destroy()
            self.new_window = Tk()
            study(self.new_window)
        pass



    def back(self, *args):
        self.root.destroy()
        pass

class create():
    def __init__(self, root):
        root.title("LBYCPA1 Project")
        root.protocol("WM_DELETE_WINDOW", lambda : exit())
        self.root = root
        ttk.Button(root, text = "Back", command = self.back).grid(column = 3, row = 4, padx = 30,sticky = E)

        style = ttk.Style()
        style.configure('Comic.TLabel', font=("Comic Sans MS", 14, "bold"))

        myLabel = ttk.Label(root, text= "CREATE", style = "Comic.TLabel")
        myLabel.grid(row = 0, column = 2, padx = 50, pady = 20)

        createinfo = "Align the question inputs with the answer inputs.\nMake sure they are of the same length.\nSeparate the questions using \"Enter\".\nAvoid empty \"Enter\" spots as they would count as an item when you study."

        Desc = ttk.Label(root, text= createinfo, style = "Comic.TLabel", justify = CENTER)
        Desc.grid(row = 1, column = 0, columnspan = 4, padx = 50, pady = 20)

        QLabel = ttk.Label(root, text= "Question", style = "Comic.TLabel")
        QLabel.grid(row = 2, column = 0, padx = 50, pady = 20)

        self.Question = Text(root,height = 10,width = 50)
        self.Question.grid(row = 3,column = 0, padx = 30, pady=30)

        ALabel = ttk.Label(root, text= "Answer", style = "Comic.TLabel")
        ALabel.grid(row = 2, column = 3, padx = 50, pady = 20)

        self.Answer = Text(root, height = 10, width = 50)
        self.Answer.grid(row = 3, column = 3, padx = 30, pady=30)
        def save():
            Answers = self.Answer.get("1.0",'end-1c')
            Questions = self.Question.get("1.0",'end-1c')

            Answers = Answers.split("\n")
            Questions = Questions.split("\n")

            try:
                assert Questions!=['']
                assert Answers!=['']
            except:
                messagebox.showerror("Empty Questions or Answers", "Make sure to input something in the text boxes")
                return

            try:
                assert len(Answers)==len(Questions)
            except:
                messagebox.showerror("Not the same number of Questions and Answers", "Make sure that the questions and answers are separated by 'enter' and they are of the same length")
            else:
                with open("data\\Flashcards.txt", mode="w+") as f:
                    for i in range(len(Questions)):
                        f.write(Questions[i])
                        f.write("\n")
                        f.write(Answers[i])
                        f.write("\n")
                messagebox.showinfo("Saved!", "Changes are made")
            pass
        ttk.Button(root, text = "Save", command = save).grid(column = 0, row = 4, padx = 30,sticky = W)

    def back(self, *args):
        self.root.destroy()
        self.new_window = Tk()
        flashcard(self.new_window)
        pass

class edit():
    def __init__(self, root):
        root.title("LBYCPA1 Project")
        root.protocol("WM_DELETE_WINDOW", lambda : exit())
        self.root = root
        ttk.Button(root, text = "Back", command = self.back).grid(column = 3, row = 4, padx = 30,sticky = E)

        style = ttk.Style()
        style.configure('Comic.TLabel', font=("Comic Sans MS", 14, "bold"))

        myLabel = ttk.Label(root, text= "EDIT", style = "Comic.TLabel")
        myLabel.grid(row = 0, column = 2, padx = 50, pady = 20)
        createinfo = "Align the question inputs with the answer inputs.\nMake sure they are of the same length.\nSeparate the questions using \"Enter\".\nAvoid empty \"Enter\" spots as they would count as an item when you study."

        Desc = ttk.Label(root, text= createinfo, style = "Comic.TLabel", justify = CENTER)
        Desc.grid(row = 1, column = 0, columnspan = 4, padx = 50, pady = 20)

        QLabel = ttk.Label(root, text= "Question", style = "Comic.TLabel")
        QLabel.grid(row = 2, column = 0, padx = 50, pady = 20)

        self.Question = Text(root,height = 10,width = 50)
        self.Question.grid(row = 3,column = 0, padx = 30, pady=30)

        ALabel = ttk.Label(root, text= "Answer", style = "Comic.TLabel")
        ALabel.grid(row = 2, column = 3, padx = 50, pady = 20)

        self.Answer = Text(root, height = 10, width = 50)
        self.Answer.grid(row = 3, column = 3, padx = 30, pady=30)

        with open("data\\flashcards\\Flashcards.txt",mode = 'r') as r:
            lines = r.readlines()
        for i in range(0,len(lines),2):
            self.Question.insert(INSERT,lines[i])
            self.Answer.insert(INSERT,lines[i+1])
            
        def save():
            Answers = self.Answer.get("1.0",'end-1c')
            Questions = self.Question.get("1.0",'end-1c')

            Answers = Answers.split("\n")
            Questions = Questions.split("\n")

            try:
                assert Questions!=['']
                assert Answers!=['']
            except:
                messagebox.showerror("Empty Questions or Answers", "Make sure to input something in the text boxes")
                return

            try:
                assert len(Answers)==len(Questions)
            except:
                messagebox.showerror("Not the same number of Questions and Answers", "Make sure that the questions and answers are separated by 'enter' and they are of the same length")
            else:
                with open("data\\flashcards\\Flashcards.txt", mode="w+") as f:
                    for i in range(len(Questions)):
                        f.write(Questions[i])
                        f.write("\n")
                        f.write(Answers[i])
                        f.write("\n")
                messagebox.showinfo("Saved!", "Changes are made")
            pass
        ttk.Button(root, text = "Save", command = save).grid(column = 0, row = 4, padx = 30,sticky = W)

    def back(self, *args):
        self.root.destroy()
        self.new_window = Tk()
        flashcard(self.new_window)
        pass

class study():
    def __init__(self, root):
        root.title("LBYCPA1 Project")
        root.protocol("WM_DELETE_WINDOW", lambda : exit())
        self.root = root
        ttk.Button(root, text = "Back", command = self.back).grid(column = 3, row = 3, padx = 30,sticky = E)

        style = ttk.Style()
        style.configure('Comic.TLabel', font=("Comic Sans MS", 14, "bold"))

        myLabel = ttk.Label(root, text= "STUDY", style = "Comic.TLabel")
        myLabel.grid(row = 0, column = 0,columnspan = 3, padx = 50, pady = 20)

        with open("data\\flashcards\\Flashcards.txt",mode = 'r') as r:
            lines = r.readlines()
        
        global counter
        counter = 0

        global Questions
        global Answers

        Questions =[lines[i] for i in range(0,len(lines),2) if lines[i] != '' and lines[i] != '\n']
        Answers = [lines[i+1] for i in range(0,len(lines),2) if lines[i+1] != '' and lines[i+1] != '\n']

        self.QuestionLabel = ttk.Label(root, text= Questions[0])
        self.QuestionLabel.grid(row = 1, column = 0,columnspan = 3, padx = 50, pady = 20)

        self.AnswerLabel = ttk.Label(self.root, text = "")
        self.AnswerLabel.grid(row = 2, column = 0,columnspan = 3, padx = 50, pady = 20)

        ttk.Button(root, text = "Show", command = self.show).grid(row = 3, column = 0, columnspan = 3, padx = 30)

    def back(self, *args):
        self.root.destroy()
        self.new_window = Tk()
        flashcard(self.new_window)
        pass

    def show(self, *args):
        global counter
        try:
            Answers[counter]
        except:
            messagebox.showinfo("Flashcards done!", "Goodjob! you completed your flashcard!")
        else:
            ttk.Button(self.root, text = "Next", command = self.nextq).grid(row = 3, column = 0, columnspan = 3, padx = 30)
            self.AnswerLabel.destroy()
            self.AnswerLabel = ttk.Label(self.root, text = Answers[counter])
            self.AnswerLabel.grid(row = 2, column = 0,columnspan = 3, padx = 50, pady = 20)
        pass

    def nextq(self, *args):
        global counter
        counter = counter + 1
        self.AnswerLabel.destroy()
        self.AnswerLabel = ttk.Label(self.root, text = "")
        self.AnswerLabel.grid(row = 2, column = 0,columnspan = 3, padx = 50, pady = 20)
        try:
            Questions[counter]
        except:
            messagebox.showinfo("Flashcards done!", "Goodjob! you completed your flashcard!")
            counter = 0
            ttk.Button(self.root, text = "Show", command = self.show).grid(row = 3, column = 0, columnspan = 3, padx = 30)
            self.QuestionLabel.destroy()
            self.QuestionLabel = ttk.Label(self.root, text= Questions[counter])
            self.QuestionLabel.grid(row = 1, column = 0,columnspan = 3, padx = 50, pady = 20)
            self.AnswerLabel.destroy()
            self.AnswerLabel = ttk.Label(self.root, text = "")
            self.AnswerLabel.grid(row = 2, column = 0,columnspan = 3, padx = 50, pady = 20)
        else:
            ttk.Button(self.root, text = "Show", command = self.show).grid(row = 3, column = 0, columnspan = 3, padx = 30)
            self.QuestionLabel.destroy()
            self.QuestionLabel = ttk.Label(self.root, text= Questions[counter])
            self.QuestionLabel.grid(row = 1, column = 0,columnspan = 3, padx = 50, pady = 20)
        pass

    