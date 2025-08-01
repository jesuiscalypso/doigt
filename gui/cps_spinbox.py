from tkinter import ttk
import tkinter as tk
from config import ClickerConfig

class CpsSpinbox(ttk.Spinbox):

    cps_indicator: tk.StringVar
    clicker_config: ClickerConfig

    def __init__(self, parent, clicker_config: ClickerConfig):
        super().__init__(master=parent)
        self.parent = parent

        self.clicker_config = clicker_config

        self.cps_indicator = tk.StringVar()
        self.cps_indicator.set(str(self.clicker_config.clicks_per_second))
        self['textvariable'] = self.cps_indicator