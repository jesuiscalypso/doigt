import flags
import keybindings

class ClickerManager():

    keybinds: keybindings.KeyBindings = keybindings.KeyBindings()
    operation_flags: flags.OperationFlags = flags.OperationFlags()

    def start(self):
        print('Hello, world!')