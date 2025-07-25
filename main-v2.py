from threading import Lock

from notifypy import Notify
from pynput import mouse
import manager

mutex = Lock()
mouse_controller = mouse.Controller()

notification = Notify()

manager = manager.ClickerManager(mouse_controller=mouse_controller, mutex=mutex,notification_manager=notification)