import pprint
import tkinter as tk
from tkinter import PhotoImage, ttk
import tkinter
from PIL import ImageTk, Image


class CreditWindow(tk.Toplevel):

    image: ImageTk.PhotoImage

    def dismiss(self):
        print("Closed window!")
        self.grab_release()
        self.destroy()

    def _setup_grid(self):
        self.columnconfigure(index=0, weight=1)
        self.rowconfigure(index=0, weight=0)
        self.rowconfigure(index=0, weight=1)
        self.rowconfigure(index=0, weight=2)

    def _setup_styles(self):
        s = ttk.Style()
        s.configure(style='Link.TLabel', foreground='green',)

    def __init__(self, parent: tk.Misc, *args, **kwargs):
        super().__init__(master=parent, *args, **kwargs)

        self.protocol("WM_DELETE_WINDOW", self.dismiss)
        
        self.title("About")
        self.resizable(False, False)
        self.geometry('200x225')

        self._setup_grid()
        self._setup_frame()
        self._setup_styles()

    def _setup_link_frame(self, parent: ttk.Widget):
        frame = ttk.Frame(master=parent)

        frame.columnconfigure(index=0, weight=1)
        frame.columnconfigure(index=1, weight=1)
        frame.rowconfigure(index=1, weight=1)

        github_link =  ttk.Label(master=frame, text='Github', underline=True, style='Link.TLabel')

        github_link.grid(column=0, row=0)

        return frame

    def _setup_frame(self) :
        frame = ttk.Frame(master=self)
        frame.grid(column=0, row=0)
        link_frame = self._setup_link_frame(parent=frame)


        imgobj = Image.open(fp='assets/placeholder.png',).resize((150,150))
        
        image = ImageTk.PhotoImage(image=imgobj)
        self.image = image


        image = ttk.Label(master=frame, image=image)

        credits = ttk.Label(master=frame, text='Made with love by Calypso\nI\'m so sorry, Orteil', anchor='center', justify='center')
        
        image.grid(column=0, row=0, sticky='nwse')
        credits.grid(column=0, row=1)
        link_frame.grid(column=0, row=2)

        