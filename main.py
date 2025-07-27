import time
from pynput import mouse, keyboard
from threading import Lock, Thread

from notifypy import Notify

import tkinter as tk
from tkinter import ttk

mutex = Lock()
mouse_controller = mouse.Controller()

# Global Hotkeys

run_clicker_hotkey = '<ctrl>+<alt>+c'
stop_clicker_hotkey = '<ctrl>+<alt>+s'
quit_program_hotkey = '<ctrl>+<alt>+q'

click_count = 100
seconds_delay = 0.1

running = False
quit_flag = False

notification = Notify()

def start_clicking():
    global running
    if running is not True:
        with mutex:
            running = True
            notification.message = "Began clicking!"
            _ = notification.send(block=False)
            

def stop_clicking():
    global running
    if running is True:
        with mutex:
            running = False
            notification.message = "Stopped clicking..."
            _ = notification.send(block=False)

def click():
    global running
    while quit_flag is not True:
        if running is True:
            mouse_controller.click(button=mouse.Button.left, count=click_count)
            time.sleep(seconds_delay)

def stop_program():
    global quit_flag
    global hotkey_listener_thread
    if quit_flag is not True:
        quit_flag = True
        hotkey_listener_thread.stop()
        print("Toggled quit flag")

hotkey_listener_thread = keyboard.GlobalHotKeys({
    run_clicker_hotkey: start_clicking,
    stop_clicker_hotkey: stop_clicking,
    quit_program_hotkey: stop_program
})

clicking_thread = Thread(target=click)

threads = [hotkey_listener_thread, clicking_thread]

# hotkey_listener_thread.start()
# clicking_thread.start()

notification.title = "Doight"
notification.message = "Started program..."
_ = notification.send(block=False)

print("Running...")

# for t in threads:
#     t.join()

# print("Exiting gracefully...")
# notification.message = "Quitting..."
# _ = notification.send(block=False)

def test():
    print("Hello, world!")

root = tk.Tk()

root.geometry("300x100")
root.title("Tkinter Thread Example")

button = ttk.Button(root, text="Start Thread", command=test)

button.pack(pady=10)

root.mainloop()