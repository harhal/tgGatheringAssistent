from typing import Any, Type
from bot.flow.step import FlowStep, StepKey

_flows: dict[str, type] = {}

class FlowSequence():
    steps: dict[str, FlowStep]
    Step: Type[StepKey]

    def __init_subclass__(cls, **kwargs: Any) -> None:
        super.__init_subclass__(**kwargs)

        if cls.Step:
            cls.Step._value2member_map_.clear()
            for member in cls.Step:
                key = f"{cls.__name__}.{member.name}"
                member._value_ = key
                cls.Step._value2member_map_[key] = member

    #@classmethod
    #def GetKey(cls):
    #    return cls.__name__