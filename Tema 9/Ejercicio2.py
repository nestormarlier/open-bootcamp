import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


class App(tk.Tk):
  def __init__(self):
    super().__init__()

    # configure the root window
    self.title('Mi segunda App')
    self.geometry('300x150')

    # label
    self.label = ttk.Label(self, text='¿Estas aprendiendo Tkinter?')
    self.label.pack()

   #list
    lista = ttk.Combobox(self, width=17, state='readonly')
    lista.place(x=30, y=80)

#desplegar
    datos = ['Python', 'Javascript', 'Java', 'C++', 'C.Net']
    lista['values'] = datos
    # button
    self.button = ttk.Button(self, text='Reset')
    self.button['command'] = self.button_clicked
    self.button.pack()

  def button_clicked(self):
    self.destroy()
    self.__init__()


if __name__ == "__main__":
  app = App()
  app.mainloop()
