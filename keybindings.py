from dataclasses import dataclass

@dataclass
class ClickerKeyBindings:
    start: str = '<ctrl>+<alt>+c'
    stop: str = '<ctrl>+<alt>+s'
    quit: str =  '<ctrl>+<alt>+q'