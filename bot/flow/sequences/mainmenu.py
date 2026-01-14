from dataclasses import dataclass
from enum import auto
from bot.flow.sequence import FlowSequence
from bot.flow.sequences.intro import Intro
from bot.flow.step import ChangeFlow, FlowSwitch, RequestInput, StepKey
from bot.handlers.base import InputHandler

@dataclass(frozen=True)
class MainMenu(FlowSequence):

    class Step(StepKey):
        SelectOption = auto()
        Switch = auto()
        ToAFlow = auto()
        ToBFlow = auto()
        ToCFlow = auto()
        ToDFlow = auto()

    steps = {
        Step.SelectOption: RequestInput(InputHandler(), Step.SelectOption),#MainMenuSelector, Step.SelectOption),
        Step.Switch: FlowSwitch(Step.SelectOption),
        Step.ToAFlow: ChangeFlow(Intro),
        Step.ToBFlow: ChangeFlow("BFlow"),
        Step.ToCFlow: ChangeFlow("CFlow"),
        Step.ToDFlow: ChangeFlow("DFlow")
    }