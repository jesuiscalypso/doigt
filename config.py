from dataclasses import dataclass
import pprint
from typing import Final
from typing import override


@dataclass
class ClickerConfig:
    _millis_per_second: Final[int]
    _sleep_interval: float
    clicks_per_second: int = 10

    def _reset_sleep_interval(self):
        self._sleep_interval = self._millis_per_second / self.clicks_per_second
        pprint.pprint(self)

    def __init__(self):
        self._millis_per_second = 1000
        self._reset_sleep_interval()

    def set_cps(self, cps: int):
        if cps > 100 or cps < 1:
            raise InvalidCpsError(cps=cps)
        self.clicks_per_second = cps
        self._reset_sleep_interval()

    def get_sleep_interval(self):
        return self._sleep_interval

class InvalidCpsError(Exception):
    def __init__(self, cps: int, msg: str ="Clicks per second must be between 1 and 100"):
        self.cps: int = cps
        self.msg: str = msg
        super().__init__(self.msg)

    @override
    def __str__(self):
        return f'{self.cps} -> {self.msg}'