from bot.api.input import InputData
from bot.handlers.base import InputHandler

class TextHandler(InputHandler):
    def ProcessInput(self, input: InputData):
        ...