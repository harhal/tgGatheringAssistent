from bot.api.input import InputData
from bot.flow.processor import FlowProcessor
from bot.session.session import SessionData

class SessionsManager():
    sessions: dict[int, SessionData]

    def __init__(self):
        ...

    def Update(self, user_id: int, input: InputData):
        if user_id not in self.sessions:
            ...
        FlowProcessor(self.sessions[user_id])