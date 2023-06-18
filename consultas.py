import tkinter as tk
from tkinter.font import Font

ancho = 272
alto = 350

class CalcPintura(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pintando el techo")
        self.geometry(f"{ancho}x{alto}")
        self.display_entry = Display(self,background="gray")
        self.display_entry.pack()
        self.display_exit = Display(self, background="black")
        self.display_exit.pack(side= tk.BOTTOM)
    
        Keyboard(self, self.click).pack()

    def click(self, tecla):
        self.display_entry.typing(tecla)


class Display(tk.Frame):
    def __init__(self, location, background="#000000"):
        super().__init__(location, width=272, height=50)
        self.pack_propagate(False)
        
        self.label = tk.Label(self, background=background, text= "", foreground="#ffffff",
                              anchor=tk.E, padx=8, 
                              font=Font(family="Arial", size="25"))
        self.label.pack(side= tk.TOP, fill =tk.BOTH, expand=True)
    def typing(self, text):
        self.label.config(text=text)


class Button(tk.Frame):
    def __init__(self, location, conector, text):
        super().__init__(location, width= 91, height=50)
        self.pack_propagate(False)
        self.conector = conector
        self.text = text
        self.button = tk.Button(self, text=text, command=self.pressed)
        self.button.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def pressed(self):
        self.conector(self.text)

class Keyboard(tk.Frame):
    def __init__(self, location, conector):
        super().__init__(location, width=272, height=300)
        Button(self, conector, "1").grid(column=0, row=3)
        Button(self, conector, "2").grid(column=1, row=3)
        Button(self, conector, "3").grid(column=2, row=3)
        Button(self, conector, "4").grid(column=0, row=2)
        Button(self, conector, "5").grid(column=1, row=2)
        Button(self, conector, "6").grid(column=2, row=2)
        Button(self, conector, "7").grid(column=0, row=1)
        Button(self, conector, "8").grid(column=1, row=1)
        Button(self, conector, "9").grid(column=2, row=1)
        Button(self, conector, "[ ]").grid(column=0, row=0)
        Button(self, conector, "O").grid(column=1, row=0)
        Button(self, conector, "L").grid(column=2, row=0)
        Button(self, conector, "ENTRY").grid(column=0, row=4, columnspan=3, sticky='WE')
c = CalcPintura()
c.mainloop()