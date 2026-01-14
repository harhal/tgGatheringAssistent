#import pytsest
#from bot.fsm import ()

from telegram import Update
from bot.api.input import InputData, InputType
from bot.handlers.texthandler import TextHandler
from bot.session.session import Session


def test_text_input_handler():
    session = Session(user_id = 123, states_stack = [], data = {})
    text_input_handler = TextHandler("test_state", "test_text_input")
    test_input = InputData(InputType.TEXT, "test_text_input_string", Update(-1))
    text_input_handler.ProcessInput(test_input)
    assert session.data["test_state"]["test_text_input"] == "test_text_input_string"