# Use Tkinter for python 2, tkinter for python 3
from tkinter import StringVar


from threading import Thread
import tkinter as tk

from manager import ClickerManager
from virtual_events import AppVirtualEvents

class MainApplication(tk.Frame):

    clicker_manager: ClickerManager
    clicker_thread: Thread

    status_text: tk.StringVar

    def on_start_click(self, event = None):
        self.status_text.set("Started clicking")

    def on_stop_click(self, event = None):
        self.status_text.set("Stopped clicking")

    def __init__(self, parent, clicker_manager: ClickerManager, *args, **kwargs) -> None:
        super().__init__(master=parent, *args, **kwargs)
        self.parent = parent
        
        self.status_text = tk.StringVar()

        self._setup_app()
        self.status_text.set("Ready to roll!")

        self.clicker_manager = clicker_manager
        self.clicker_thread = Thread(target=clicker_manager.run, daemon=True)
        self.clicker_thread.start()


        self.pack()
    
    def _setup_app(self) -> None:
        
        label = tk.Label(master=self)
        label['textvariable'] = self.status_text

        

        label.pack()