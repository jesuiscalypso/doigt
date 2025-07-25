from dataclasses import dataclass


@dataclass
class ClickerConfig:
    click_count: int = 100
    seconds_delay: float = 0.1