from hmac import new
import pprint
from tkinter import ttk
import tkinter as tk
from config import ClickerConfig

class CpsSpinbox(ttk.Spinbox):

    cps_indicator: tk.StringVar
    clicker_config: ClickerConfig

    def _validate_cps_spinbox_value(self, newval: str):
        new_value = None

        try:
            new_value = int(newval)
        except:
            return False

        if new_value < 1 or new_value > 100:
            return False
        
        return True

    def _cps_spinbox_value_change(self, internal_var_name: str, internal_var_index: str, operation: str) -> object:
        
        numerical_value: int | None = None

        try:
            numerical_value = int(self.cps_indicator.get())
        except ValueError as e:
            print("Error in cps spinbox")
            raise e

        self.clicker_config.set_cps(cps=numerical_value)

        print(self.cps_indicator.get())

    def __init__(self, parent: tk.Widget, clicker_config: ClickerConfig):
        
        validation = parent.register(func=self._validate_cps_spinbox_value)

        validation_wrapper = (validation, "%P")
        
        super().__init__(master=parent,validate='key', validatecommand=validation_wrapper)
        self.parent = parent

        self.clicker_config = clicker_config

        self.cps_indicator = tk.StringVar()
        self.cps_indicator.set(str(self.clicker_config.clicks_per_second))
        _ = self.cps_indicator.trace_add(mode='write', callback=self._cps_spinbox_value_change)
        self['textvariable'] = self.cps_indicator

        self['validatecommand'] = validation_wrapper


        