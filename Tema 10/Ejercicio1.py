import tkinter as tk 
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Mi primer App')
        self.geometry('300x100')
            
        self.label = ttk.Label(self, text = "¿Estas aprendiendo Tkinter?")
        self.label.pack()

        self.radio1=ttk.Radiobutton(self, text="Verdadero", value=True)
        self.radio1.pack()
        self.radio2=ttk.Radiobutton(self, text="Falso", value=False)
        self.radio2.pack()

        self.button=ttk.Button(self, text="Reset")
        self.button['command']=self.button_clicked
        self.button.pack()

    def button_clicked(self):
        self.destroy()
        self.__init__()

if __name__=='__main__':
    app = App()
    app.mainloop()