from tkinter import Tk, Frame, Checkbutton
from tkinter import BooleanVar, BOTH

class Example(Frame):
    def __init__(self):
        super().__init__()
        self.initUI()
 
    def initUI(self):
        self.master.title("Флажки")
        self.pack(fill=BOTH, expand=True)
        self.var = BooleanVar()
 
        cb = Checkbutton(
            self, 
            text="Показать заголовок", 
            variable=self.var, 
            command=self.onClick)
        cb.select()
        cb.place(x=50, y=50)

    def onClick(self):
        if self.var.get():
            self.master.title("Флажки")
        else:
           self.master.title("")
 
 
def main():
    root = Tk()
    root.geometry("250x150+300+300")
    app = Example()
    root.mainloop()
 
 
if __name__ == '__main__':
    main()