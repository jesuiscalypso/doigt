from threading import Lock, Thread

from notifypy import Notify
from pynput import mouse
import manager

import tkinter as tk
from tkinter import ttk

# Initial setup

mutex = Lock()
mouse_controller = mouse.Controller()

notification = Notify()

manager = manager.ClickerManager(mouse_controller=mouse_controller, mutex=mutex,notification_manager=notification)

manager_thread = Thread(target=manager.run)

# GUI setup

def start_manager():
    manager_thread.start()


root = tk.Tk()

icon_path = 'assets/pointer.png'
icon_image = tk.PhotoImage(file=icon_path)
root.iconphoto(False, icon_image)
root.geometry("300x100")
root.title("Doigt")

button = ttk.Button(root, text="Start Thread", command=manager.run)

button.pack(pady=10)

root.mainloop()