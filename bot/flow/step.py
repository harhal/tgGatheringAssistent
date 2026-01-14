from dataclasses import dataclass
from enum import StrEnum
from typing import Any, Type
from bot.flow.sequence import FlowSequence
from bot.flow.steps.drafthandler import DraftHandler
from bot.flow.steps.switchhandler import SwitchHandler
from bot.handlers.base import InputHandler
from bot.ui.localization import Loc

class StepKey(StrEnum):
    __index_to_value__: list[StrEnum]
    __value_to_index__: dict[StrEnum, int]

    @classmethod
    def __check_cash__(cls):
        if len(cls.__index_to_value__) == len(cls.__members__.values()):
            return
        cls.__index_to_value__ = list(cls.__members__.values())
        cls.__value_to_index__ = {key: i for i, key in enumerate(cls.__index_to_value__)}

    @classmethod
    def GetFirstStep(cls):
        cls.__check_cash__()
        return next(iter(cls))
    
    def GetNextStep(self):
        self.__class__.__check_cash__()
        next_idx = self.__class__.__value_to_index__[self] + 1
        if next_idx > len(self.__class__.__index_to_value__):
            return None
        return self.__class__.__index_to_value__[next_idx]

class FlowStep():
    ...

@dataclass
class RequestInput(FlowStep):
    handler: InputHandler
    cash_draft_key: str

@dataclass
class RequestData(FlowStep):
    ...

@dataclass
class UpdateDraft(FlowStep):
    handler: DraftHandler

@dataclass
class PublishDraft(FlowStep):
    ...

@dataclass
class ChangeFlow(FlowStep):
    flow: Type[FlowSequence]
    step: StepKey | None = None

@dataclass
class SendMessage(FlowStep):
    msg_loc_key: str
    draft_keys: list[str] | dict[Loc.FieldKey, str] | None = None

    def GetMessage(self, draft: dict[str, Any], loc: Loc):
        if isinstance(self.draft_keys, list):
            return loc.LocalizeMessage(self.msg_loc_key, [draft[key] for key in self.draft_keys])
        if isinstance(self.draft_keys, dict):
            return loc.LocalizeMessage(self.msg_loc_key, {loc_field_key: draft[draft_key] for loc_field_key, draft_key in self.draft_keys.items()})

@dataclass
class FlowSwitch(FlowStep):
    handler: SwitchHandler

@dataclass
class FinishSession(FlowStep):
    ...