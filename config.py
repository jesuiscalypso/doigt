from dataclasses import dataclass


@dataclass
class ClickerConfig:
    sleep_interval: float
    clicks_per_second: int = 1000

    def __init__(self):
        millis_per_second = 1000
        self.sleep_interval = millis_per_second / self.clicks_per_second