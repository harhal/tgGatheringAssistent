from dataclasses import dataclass

from bot.flow.step import StepKey

@dataclass
class SwitchHandler():
    switch_draft_key: str

    def SwitchStep(self) -> StepKey:
        raise NotImplementedError()