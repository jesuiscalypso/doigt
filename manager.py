from dataclasses import dataclass
import pprint
from threading import Thread
from typing import Callable
import pynput
from pynput import mouse
from config import ClickerConfig

import time

import config
import flags
import keybindings

from notifypy import Notify

from _thread import LockType

@dataclass
class ClickerManagerCallbacks:
    on_start_click:Callable[[], None]
    on_stop_click:Callable[[], None]

class ClickerManager():
    
    notification: Notify
    mouse_controller: pynput.mouse.Controller
    mutex: LockType

    keybinds: keybindings.ClickerKeyBindings = keybindings.ClickerKeyBindings()
    operation_flags: flags.ClickerFlags = flags.ClickerFlags()
    configuration: ClickerConfig =  config.ClickerConfig()

    hotkey_thread: pynput.keyboard.GlobalHotKeys

    callbacks: ClickerManagerCallbacks

    def __init__(self, notification_manager: Notify, mouse_controller: pynput.mouse.Controller, mutex: LockType, callbacks: ClickerManagerCallbacks):
        self.notification = notification_manager
        self.mouse_controller = mouse_controller
        self.mutex = mutex

        hotkey_listener_thread = pynput.keyboard.GlobalHotKeys(hotkeys={
            self.keybinds.start: self.start,
            self.keybinds.stop: self.stop,
            # self.keybinds.quit: self.quit
        })

        self.hotkey_thread = hotkey_listener_thread

        self.callbacks = callbacks

        pprint.pprint(self.configuration)
        

    def _click(self):
        while self.operation_flags.should_stop is False:
            if self.operation_flags.is_clicking is True:
                self.mouse_controller.click(button=mouse.Button.left, count=1)
                time.sleep(self.configuration.get_sleep_interval() / 1000 ) # Sleep interval is in millis, so we must convert
            else:
                time.sleep(1) # We don't want to be hogging cpu time with this thread.
        print("Joining the clicking thread")


    def run(self):

        self.operation_flags.should_stop = False

        if self.operation_flags.has_started_once is False:
            self.operation_flags.has_started_once = True
            self.hotkey_thread.start()

        clicking_thread = Thread(target=self._click)
        clicking_thread.start()

        print("Running!")

        

    def start(self):
        with self.mutex:
            self.operation_flags.is_clicking = True
            self.callbacks.on_start_click()
        print('Start!')
        print(str(self.operation_flags))

    def stop(self):
        with self.mutex:
            self.operation_flags.is_clicking = False
            self.callbacks.on_stop_click()
        print('Stop!')
        print(str(self.operation_flags))

    #def quit(self):
    #    self.operation_flags.should_stop = True
    #    print('Quit!')
            