import time
from pynput import mouse, keyboard
from threading import Lock, Thread

mutex = Lock()
mouse_controller = mouse.Controller()

# global hotkeys

run_clicker_hotkey = '<ctrl>+<alt>+c'
stop_clicker_hotkey = '<ctrl>+<alt>+s'
quit_program_hotkey = '<ctrl>+<alt>+q'

click_count = 100
seconds_delay = 0.1

running = False
quit_flag = False

def start_clicking():
    global running
    if running is not True:
        with mutex:
            running = True
            print("Started!")
            

def stop_clicking():
    global running
    if running is True:
        with mutex:
            running = False
            print("Stopped!")

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

hotkey_listener_thread.start()
clicking_thread.start()


print("Running...")

for t in threads:
    t.join()

print("Exiting gracefully...")