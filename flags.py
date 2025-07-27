from dataclasses import dataclass

@dataclass
class ClickerFlags:
    is_clicking: bool = False
    should_stop: bool = False
    has_started_once: bool = False