import tkinter as tk
from tkinter import ttk

class CreditWindow(tk.Toplevel):

    def dismiss(self):
        print("Closed window!")
        self.grab_release()
        self.destroy()

    def _setup_grid(self):
        self.columnconfigure(index=0, weight=1)
        self.columnconfigure(index=1, weight=1)
        self.rowconfigure(index=0, weight=1)

    def __init__(self, parent: tk.Misc, *args, **kwargs):
        super().__init__(master=parent, *args, **kwargs)
        self.protocol("WM_DELETE_WINDOW", self.dismiss)

        

    def _setup_frame(self) :
        frame = ttk.Frame(master=self)

        

        frame.grid(column=0, row=0)
        