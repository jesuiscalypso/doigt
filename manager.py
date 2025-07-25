import pynput
from config import ClickerConfig


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

    def __init__(self, notification_manager: Notify, mouse_controller: pynput.mouse.Controller, mutex: LockType):
        self.notification = notification_manager
        self.mouse_controller = mouse_controller
        self.mutex = mutex
        self.run()

    def run(self):
        print("Running!")
        

    def start(self):
        print('Hello, world!')