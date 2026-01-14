
from dataclasses import dataclass
from enum import StrEnum, auto
from typing import Any
from telegram import Update

class InputType(StrEnum):
    TEXT = auto()
    BUTTON = auto()
    CONTACT = auto()
    WEBAPP = auto()
    LOCATION = auto()
    FILE = auto()
    IMAGE = auto()
    VIDEO = auto()
    REPLY = auto()
    COMMAND = auto()
    UNKNOWN = auto()

@dataclass
class InputData:
    type: InputType
    content: Any
    raw: Update