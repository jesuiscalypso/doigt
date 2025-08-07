from tkinter import Tk
import tkinter as tk

from threading import Lock
from notifypy import Notify
from pynput import mouse

from gui.main_app import MainApplication
from manager import ClickerManager, ClickerManagerCallbacks
from virtual_events import AppVirtualEvents

def setup_root() -> Tk:
    root = tk.Tk()

    icon_path = 'assets/pointer.png'
    icon_image = tk.PhotoImage(file=icon_path)
    root.iconphoto(False, icon_image)

    root.geometry("300x100")
    root.title("Doigt")
    
    root.wm_attributes("-topmost", 1)

    root.resizable(False, False)
    
    _ = root.columnconfigure(index=0, weight=1)
    _ = root.rowconfigure(index=0, weight=1)

    return root

def on_start_click(gui_root: Tk):
    gui_root.event_generate(sequence=AppVirtualEvents.start_click)
    print("Fired start event")

def on_stop_click(gui_root: Tk):
    gui_root.event_generate(sequence=AppVirtualEvents.stop_click)
    print("Fired stop event")

def setup_main_app(app_root: Tk) -> ClickerManager:
    
    # Initial setup

    mutex = Lock()
    mouse_controller = mouse.Controller()

    notification = Notify()

    clicker_manager = ClickerManager(
        mouse_controller=mouse_controller, 
        mutex=mutex,
        notification_manager=notification,
        callbacks= ClickerManagerCallbacks(
            on_start_click= lambda: on_start_click(gui_root=app_root),
            on_stop_click= lambda: on_stop_click(gui_root=app_root)
        ), 
    )
    
    return clicker_manager

def setup_global_event_bindings(root: Tk, app: MainApplication):
    _ = root.bind(AppVirtualEvents.start_click, app.on_start_click)
    _ = root.bind(AppVirtualEvents.stop_click, app.on_stop_click)

def start_app():
    root = setup_root()
    clicker_manager = setup_main_app(root)

    main_app: MainApplication = MainApplication(parent=root, clicker_manager=clicker_manager)

    setup_global_event_bindings(root, main_app)

    root.mainloop()

if __name__ == '__main__':
    start_app()