from dataclasses import dataclass

@dataclass
class KeyBindings:
    start: str = '<ctrl>+<alt>+c'
    stop: str = '<ctrl>+<alt>+s'
    quit: str =  '<ctrl>+<alt>+q'