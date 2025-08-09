from threading import Lock
import tkinter as tk

from notifypy import Notify
from pynput import mouse

from credit import CreditWindow
from gui.main_app import MainApplication
from manager import ClickerManager, ClickerManagerCallbacks
from virtual_events import AppVirtualEvents


class ApplicationMenu(tk.Menu):

    parent: tk.Misc
    about_menu: tk.Menu

    credit_window: CreditWindow | None = None
    
    def _open_credit_window(self):
        self.credit_window = CreditWindow(self)

    def __init__(self, parent: tk.Misc, *args, **kwargs):
        super().__init__(master=parent, *args, **kwargs)

        self.parent = parent
        parent['menu'] = self

        self._setup_info_menu()

    def _setup_info_menu(self):
        about = tk.Menu(master=self)

        self.add_cascade(menu=about, label='Help')
        about.add_command(label='About Doigt', command=self._open_credit_window)
        
        self.about_menu = about


class ApplicationRoot(tk.Tk):

    main_frame: MainApplication
    menubar: ApplicationMenu

    def _on_start_click(self):
        self.event_generate(sequence=AppVirtualEvents.start_click)

    def _on_stop_click(self):
        self.event_generate(sequence=AppVirtualEvents.stop_click)


    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._setup_window()
        self._setup_main_app()
        self._setup_menu()
        self._setup_global_bindings()

    def _setup_window(self):

        icon_path = 'assets/pointer.png'
        icon_image = tk.PhotoImage(file=icon_path)
        self.iconphoto(False, icon_image)

        self.geometry("350x125")
        self.title("Doigt")
        
        # self.wm_attributes("-topmost", 1)
        self.option_add(pattern='*tearOff', value=False)
        self.resizable(False, False)
        
        _ = self.columnconfigure(index=0, weight=1)
        _ = self.rowconfigure(index=0, weight=1)

    def _setup_menu(self):
        self.menubar = ApplicationMenu(parent=self)

    def _setup_main_app(self):
        # Initial setup

        mutex = Lock()
        mouse_controller = mouse.Controller()

        notification = Notify()

        clicker_manager = ClickerManager(
            mouse_controller=mouse_controller, 
            mutex=mutex,
            notification_manager=notification,
            callbacks= ClickerManagerCallbacks(
                on_start_click= lambda: self._on_start_click(),
                on_stop_click= lambda: self._on_stop_click()
            ), 
        )
        
        main_frame: MainApplication = MainApplication(parent=self, clicker_manager=clicker_manager)

        self.main_frame = main_frame

    def _setup_global_bindings(self):
        _ = self.bind(AppVirtualEvents.start_click, self.main_frame.on_start_click)
        _ = self.bind(AppVirtualEvents.stop_click, self.main_frame.on_stop_click)


