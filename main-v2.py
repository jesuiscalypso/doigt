from threading import Lock

from notifypy import Notify
from pynput import mouse

import tkinter as tk
from gui.main_app import MainApplication

import manager

def setup_root():
    root = tk.Tk()

    icon_path = 'assets/pointer.png'
    icon_image = tk.PhotoImage(file=icon_path)
    root.iconphoto(False, icon_image)

    root.geometry("300x100")
    root.title("Doigt")

    return root

def setup_main_app(): 
    # Initial setup
    mutex = Lock()
    mouse_controller = mouse.Controller()

    notification = Notify()

    clicker_manager = manager.ClickerManager(mouse_controller=mouse_controller, mutex=mutex,notification_manager=notification)
    
    return clicker_manager

root = setup_root()
clicker_manager = setup_main_app()
main_app = MainApplication(parent=root, clicker_manager=clicker_manager)
root.mainloop()