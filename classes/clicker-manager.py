import time
from notifypy.notify import Notify


from classes.keybinds import Keybinds
from classes import keybinds

from pynput.mouse._base import Controller


from threading import Lock, Thread
from _thread import LockType

from pynput import keyboard, mouse
from notifypy import Notify

from main import clicking_thread

class ClickerManager:

    mutex: LockType = Lock()
    mouse_controller: Controller = mouse.Controller()
    keybinds: Keybinds = keybinds.Keybinds()

    click_count: int = 100
    seconds_delay: float = 0.1

    running: bool = False
    quit_flag: bool = False

    notification: Notify = Notify()

    def __init__(self):
       

    def start_clicking(self):
        if self.running is not True:
            with self.mutex:
                self.running = True
                self.notification.message = "Began clicking!"
                _ = self.notification.send(block=False)
                

    def stop_clicking(self):
        if self.running is True:
            with self.mutex:
                self.running = False
                self.notification.message = "Stopped clicking..."
                _ = self.notification.send(block=False)

    def click(self):
        while self.quit_flag is not True:
            if self.running is True:
                self.mouse_controller.click(button=mouse.Button.left, count=self.click_count)
                time.sleep(self.seconds_delay)

    def stop_program(self):
        if self.quit_flag is not True:
            self.quit_flag = True
            self.hotkey_listener_thread.stop()
            print("Toggled quit flag")