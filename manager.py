from threading import Thread
import pynput
from pynput import mouse
from config import ClickerConfig

import time

import config
import flags
import keybindings

from notifypy import Notify

from _thread import LockType

class ClickerManager():

    keybinds: keybindings.ClickerKeyBindings = keybindings.ClickerKeyBindings()
    operation_flags: flags.ClickerFlags = flags.ClickerFlags()
    configuration: ClickerConfig =  config.ClickerConfig()

    notification: Notify
    mouse_controller: pynput.mouse.Controller

    mutex: LockType

    hotkey_thread: pynput.keyboard.GlobalHotKeys

    stop_flag: bool = False

    def __init__(self, notification_manager: Notify, mouse_controller: pynput.mouse.Controller, mutex: LockType):
        self.notification = notification_manager
        self.mouse_controller = mouse_controller
        self.mutex = mutex
        
        hotkey_listener_thread = pynput.keyboard.GlobalHotKeys(hotkeys={
            self.keybinds.start: self.start,
            self.keybinds.stop: self.stop,
            self.keybinds.quit: self.quit
        })

        self.hotkey_thread = hotkey_listener_thread
        

    def _click(self):
        while self.stop_flag is False:
            if self.operation_flags.is_clicking is True:
                self.mouse_controller.click(button=mouse.Button.left, count=self.configuration.click_count)
                time.sleep(self.configuration.seconds_delay)
        print("Joining the clicking thread")


    def run(self):

        

        clicking_thread = Thread(target=self._click)
        clicking_thread.start()

        print("Running!")

        self.hotkey_thread.start()

        self.hotkey_thread.join()
        clicking_thread.join()

    def start(self):
        with self.mutex:
            self.operation_flags.is_clicking = True
        print('Start!')
        print(str(self.operation_flags))

    def stop(self):
        with self.mutex:
            self.operation_flags.is_clicking = False
        print('Stop!')
        print(str(self.operation_flags))

    def quit(self):
        self.stop_flag = True
        self.hotkey_thread.stop()
        print('Quit!')
            