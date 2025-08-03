from hmac import new
import pprint
from tkinter import ttk
import tkinter as tk
from config import ClickerConfig

class CpsSpinbox(ttk.Spinbox):

    cps_indicator: tk.StringVar
    clicker_config: ClickerConfig

    @staticmethod
    def _validate_cps_spinbox_value(newval: str):
        new_value = None

        try:
            new_value = int(newval)
        except:
            return False

        if new_value <= 0:
            return False
        
        return True

    def __init__(self, parent: tk.Widget, clicker_config: ClickerConfig):
        
        validation = parent.register(func=self._validate_cps_spinbox_value)

        validation_wrapper = (validation, "%P")
        
        super().__init__(master=parent,validate='key', validatecommand=validation_wrapper)
        self.parent = parent

        self.clicker_config = clicker_config

        self.cps_indicator = tk.StringVar()
        self.cps_indicator.set(str(self.clicker_config.clicks_per_second))
        self['textvariable'] = self.cps_indicator

        self['validatecommand'] = validation_wrapper


        