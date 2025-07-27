
from dataclasses import dataclass


@dataclass
class Keybinds:
    run_clicker: str = '<ctrl>+<alt>+c'
    stop_clicker: str = '<ctrl>+<alt>+s'
    quit_program: str = '<ctrl>+<alt>+q'