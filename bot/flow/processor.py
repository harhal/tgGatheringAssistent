from bot.api.input import InputData
from bot.flow.flowdata import FlowData
from bot.flow.step import ChangeFlow, FinishSession, FlowSwitch, PublishDraft, RequestData, RequestInput, SendMessage, UpdateDraft
from bot.session.session import SessionData


class FlowProcessor():
    session_data: SessionData

    def __init__(self, session_data: SessionData):
        self.session_data = session_data

    def Update(self, input: InputData):
        session_data = self.session_data
        session_data.ConsumeInput(input)

        while True:
            curr_step = session_data.GetStep()
            match curr_step:
                case RequestData():
                    ...
                case UpdateDraft(handler):
                    handler.UpdateDraft(self.session_data.draft)
                case PublishDraft():
                    ...
                case RequestInput(handler):
                    session_data.input_handler = handler
                    return
                case SendMessage():
                    ...
                case FlowSwitch(handler):
                    session_data.flow.step = handler.SwitchStep()
                case ChangeFlow(flow, step):
                    session_data.flow = FlowData(flow, step)
                case FinishSession():
                    #rise signal to clean all user's data and abort session
                    ...
                case _:
                    ...