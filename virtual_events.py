from dataclasses import dataclass
from typing import Final


@dataclass
class AppVirtualEvents:
    start_click: Final[str] = "<<StartClick>>"
    stop_click: Final[str] = "<<StopClick>>"