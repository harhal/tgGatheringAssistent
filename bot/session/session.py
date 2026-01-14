from dataclasses import dataclass
from typing import Any
from bot.api.input import InputData
from bot.flow.flowdata import FlowData
from bot.handlers.base import InputHandler
from bot.session.userid import UserId

@dataclass
class SessionData:
    user_id: UserId
    input_handler: InputHandler
    flow: FlowData
    draft: dict[str, Any]

    def ConsumeInput(self, input: InputData):
        ...

    def GetStep(self):
        return self.flow.GetStep()