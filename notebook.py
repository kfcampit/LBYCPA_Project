from tkinter import *
from tkinter import ttk
from tkinter.font import Font

class notebookMain:
    def __init__(self, root):
        self.root = root
        root.title("LBYCPA1 Project")
        root.protocol("WM_DELETE_WINDOW", lambda : exit())

        mainframe = Frame(root)
        mainframe.grid(column = 0, row = 0)

        Button(mainframe, text = "Pop - up", command = self.notebookPopUp).grid(column = 1, row = 1)

        root.mainloop()

    def notebookPopUp (self):
        root = Toplevel()
        root.title("LBYCPA1 Project")

        root.geometry("600x200")

        canvasOne = Canvas(root)
        frameOne = Frame(canvasOne)
        Label(frameOne, text="hello")

        canvas = Canvas(root)
        scroll_y = Scrollbar(root, orient="vertical", command=canvas.yview)

        frame = Frame(canvas)
        
        for i in range(1, 100):
            Label(frame, text='test %i' % i, width = 48, justify = "left").grid(column = 0, row = i, padx = 8, pady = 8)
            Button(frame, text = "test", width = 12).grid(column = 4, row = i, padx = 4)
            Button(frame, text = "test", width = 12).grid(column = 5, row = i, padx = 4)
        canvas.create_window(0, 0, anchor='nw', window=frame)

        canvas.update_idletasks()

        canvas.configure(scrollregion=canvas.bbox('all'), yscrollcommand=scroll_y.set)
                        
        canvas.pack(fill='both', expand=True, side='left')
        scroll_y.pack(fill='y', side='right')

class notebookCreate:
    def __init__(self, root):
        self.root = root
        root.title("LBYCPA1 Project")

class notebookEdit:
    def __init__(self, root):
        self.root = root
        root.title("LBYCPA1 Project")

root = Tk()
notebookMain(root)