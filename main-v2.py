from threading import Lock

from notifypy import Notify
from pynput import mouse
import manager

import tkinter as tk
from tkinter import ttk

mutex = Lock()
mouse_controller = mouse.Controller()

notification = Notify()

manager = manager.ClickerManager(mouse_controller=mouse_controller, mutex=mutex,notification_manager=notification)

root = tk.Tk()

root.geometry("300x100")
root.title("Tkinter Thread Example")

button = ttk.Button(root, text="Start Thread", command=manager.run)

button.pack(pady=10)

root.mainloop()