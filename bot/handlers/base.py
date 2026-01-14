from abc import abstractmethod

from bot.api.input import InputData

class InputHandler():
    #def __init__(self, state_key: str, data_key: str):
    #    self.state_key = state_key
    #    self.data_key = data_key

    @abstractmethod
    def ValidateInput(self, input: InputData) -> bool:
        ...

    @abstractmethod
    def ProcessInput(self, input: InputData) -> object:
        ...