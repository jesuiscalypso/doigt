# Use Tkinter for python 2, tkinter for python 3
import tkinter as tk

from manager import ClickerManager

class MainApplication(tk.Frame):

    clicker_manager: ClickerManager

    def __init__(self, parent, clicker_manager: ClickerManager, *args, **kwargs):
        tk.Frame.__init__(self, master=parent, *args, **kwargs)
        self.parent = parent
        self.clicker_manager = clicker_manager
    