import pprint
import tkinter as tk
from tkinter import PhotoImage, ttk
import tkinter
from PIL import ImageTk, Image
import webbrowser



class AboutWindow(tk.Toplevel):

    parent: tk.Tk

    github_link: str = "https://github.com/jesuiscalypso"

    link_frame: ttk.Frame
    github_image: ImageTk.PhotoImage

    image: ImageTk.PhotoImage

    def _open_github(self):
        _ = webbrowser.open(url=self.github_link)

    def dismiss(self):
        print("Closed window!")
        self.grab_release()
        self.destroy()
        self.parent.deiconify()

    def _setup_grid(self):
        self.columnconfigure(index=0, weight=1)
        self.rowconfigure(index=0, weight=0)
        self.rowconfigure(index=0, weight=1)
        self.rowconfigure(index=0, weight=2)

    def _setup_styles(self):
        s = ttk.Style()
        s.configure(style='Link.TLabel', foreground='green',)

    def __init__(self, parent: tk.Tk, *args, **kwargs):
        super().__init__(master=parent, *args, **kwargs)
        self.parent = parent

        self.protocol("WM_DELETE_WINDOW", self.dismiss)
        
        self.title("Abouts")
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

        icon_path = 'assets/pointer.png'
        icon_image = tk.PhotoImage(file=icon_path)
        self.iconphoto(False, icon_image)

        imageobj = Image.open(fp='assets/github.png').resize(size=(25,25))
        image = ImageTk.PhotoImage(imageobj)
        self.github_image = image

        github_button =  ttk.Button(master=frame, image=image, underline=True, cursor='hand2', command=self._open_github)

        github_button.grid(column=0, row=0)

        return frame

    def _setup_frame(self) :
        frame = ttk.Frame(master=self)
        self._setup_link_frame(parent=frame)
        
        
        imgobj = Image.open(fp='assets/scuff.png',).resize((150,150))
        image = ImageTk.PhotoImage(image=imgobj)
        
        self.image = image
        self.link_frame = self._setup_link_frame(parent=frame)

        image = ttk.Label(master=frame, image=image)

        about = ttk.Label(master=frame, text='Made by Calypso, with love.\nI\'m so sorry, Orteil', anchor='center', justify='center')
        
        frame.grid(column=0, row=0)
        
        image.grid(column=0, row=0, sticky='nwse')
        about.grid(column=0, row=1)
        self.link_frame.grid(column=0, row=2)

        