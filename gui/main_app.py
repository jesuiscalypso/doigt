# Use Tkinter for python 2, tkinter for python 3
from tkinter import StringVar


from threading import Thread
import tkinter as tk
from tkinter import ttk

from gui.cps_spinbox import CpsSpinbox
from manager import ClickerManager

class MainApplication(ttk.Frame):
    

    clicker_manager: ClickerManager
    
    clicker_thread: Thread

    status_text: tk.StringVar
    cps_text: tk.StringVar

    def on_start_click(self, event = None):
        self.status_text.set("Started clicking")

    def on_stop_click(self, event = None):
        self.status_text.set("Stopped clicking")

    def __init__(self, parent, clicker_manager: ClickerManager, *args, **kwargs) -> None:
        super().__init__(master=parent, *args, **kwargs)
        self.parent = parent
        
        self.status_text = tk.StringVar()
        self.status_text.set("Ready to roll!")

        self.clicker_manager = clicker_manager

        self.cps_text = tk.StringVar()
        self.cps_text.set(value=str(self.clicker_manager.configuration.clicks_per_second))

        self.clicker_thread = Thread(target=clicker_manager.run, daemon=True)
        
        self._setup_app()
        
        self.clicker_thread.start()
        self.grid(column=0, row=0)
    
    def _setup_app(self) -> None:
        
        status_label = tk.Label(master=self, justify='center')
        status_label['textvariable'] = self.status_text
        
        # cps_spinbox = ttk.Spinbox(master=self, from_=1, to=100, increment=1)
        # cps_spinbox['textvariable'] = self.cps_text

        cps_spinbox = CpsSpinbox(parent=self, clicker_config=self.clicker_manager.configuration)

        status_label.grid(column=0, row=0)
        cps_spinbox.grid(column=0, row=2)