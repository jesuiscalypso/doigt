# Use Tkinter for python 2, tkinter for python 3
from tkinter import Misc

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

    cps_spinbox: CpsSpinbox
    status_label: tk.Label

    def on_start_click(self, event = None):
        
        self.status_text.set(value="Clicking")
        self.status_label.config(fg="green")
        self.cps_spinbox.state(statespec=['disabled'])

    def on_stop_click(self, event = None):
        self.status_text.set(value="Not clicking")
        self.status_label.config(fg="red")
        self.cps_spinbox.state(statespec=['!disabled'])

    def __init__(self, parent: Misc, clicker_manager: ClickerManager, *args, **kwargs) -> None:

        self._build_style()
        super().__init__(master=parent, *args, **kwargs)
        self.parent: Misc = parent

        self.clicker_manager = clicker_manager
        self._setup_vars()
        self._setup_grid()
        self._setup_widgets()

        self.clicker_thread = Thread(target=clicker_manager.run, daemon=True)
        self.clicker_thread.start()
    
    def _build_style(self) -> None:
        s = ttk.Style()

    def _setup_vars(self)-> None:
        self.status_text = tk.StringVar()
        self.status_text.set("Not clicking.")

        self.cps_text = tk.StringVar()
        self.cps_text.set(value=str(self.clicker_manager.configuration.clicks_per_second))

    def _setup_grid(self)-> None:
        self.grid(column=0, row=0, sticky='nswe')
        self.columnconfigure(index=0, weight=1)
        self.rowconfigure(index=0, weight=1)
        self.rowconfigure(index=1, weight=1)
        self.rowconfigure(index=2, weight=1)
        self.rowconfigure(index=3, weight=1)
        self.rowconfigure(index=4, weight=1)
    
    def _setup_widgets(self) -> None:
        
        status_label = tk.Label(master=self, justify='center', fg="red")
        status_label['textvariable'] = self.status_text
        self.status_label = status_label

        start_click_label = tk.Label(self, justify='center', fg="gray", text="CTRL + ALT + C to start clicking")
        stop_click_label = tk.Label(self, justify='center', fg="gray", text="CTRL + ALT + S to stop")
        cps_info_label = tk.Label(self, justify='center', fg="black", text="Clicks per second:")

        cps_spinbox = CpsSpinbox(parent=self, clicker_config=self.clicker_manager.configuration)

        status_label.grid(column=0, row=0, sticky='nsew')
        start_click_label.grid(column=0, row=1, sticky='nsew')
        stop_click_label.grid(column=0, row=2, sticky='nsew')
        cps_info_label.grid(column=0, row=3, sticky='nsew')
        cps_spinbox.grid(column=0, row=4, sticky='')

        self.cps_spinbox = cps_spinbox