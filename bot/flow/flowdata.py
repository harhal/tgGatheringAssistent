from typing import Type
from bot.flow.sequence import FlowSequence
from bot.flow.step import StepKey

class FlowData():
    flow: Type[FlowSequence]
    step: StepKey

    def __init__(self, flow: Type[FlowSequence], step: StepKey | None) -> None:
        self.flow = flow
        if step:
            self.step = step
        else:
            self.step = flow.Step.GetFirstStep()

    def GetStep(self):
        return self.flow.steps[self.step]