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
        session_data = self.sessions[user_id]
        if not session_data.input_handler.HandleInput(input, session_data.draft)
            return
        session_data.input_handler = BlockInput()
        
        flow = FlowProcessor(session_data)
        for request in flow.Update()
            match request:
                case TGRequest():
                    ...
                    if isinstance(request, TGInputRequest)
                        session_data.input_handler 
                case GCRequest():
                    ...
                case DBRequest():