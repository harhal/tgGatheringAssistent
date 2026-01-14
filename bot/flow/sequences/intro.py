from dataclasses import dataclass
from enum import auto
from bot.flow.sequence import FlowSequence
from bot.flow.sequences.mainmenu import MainMenu
from bot.flow.step import ChangeFlow, SendMessage, StepKey
from bot.ui.localization import Loc


@dataclass(frozen=True)
class Intro(FlowSequence):

    class Step(StepKey):
        IntroMessage = auto()
        ToMainMenu = auto()

    steps = {
        Step.IntroMessage: SendMessage(Step.IntroMessage),
        Step.ToMainMenu: ChangeFlow(MainMenu)
    }

    Loc.NewChecks(Step.IntroMessage)