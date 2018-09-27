import pandas as pd
from random import randint, choice
import numpy as np
from numpy.random import choice
from sklearn.svm import SVR
import pickle
import warnings
from ControllerSetup.twoPointfunc import goForTwo
from ControllerSetup.twoPointAgg import goForTwoAgg

warnings.filterwarnings("ignore")

dfOffPlaybook = pd.read_csv("C:/Temp/Madden/ControllerSetup/playbooks/offPlaybook2.csv")
dfDefPlaybook = pd.read_csv("C:/Temp/Madden/ControllerSetup/playbooks/defPlaybook.csv")

dfTexanPlaybook = pd.read_csv("C:/Temp/MaddenImage/ControllerSetup/playbooks/TexansFormations.csv")
dfColtPlaybook = pd.read_csv("C:/Temp/MaddenImage/ControllerSetup/playbooks/ColtsFormations.csv")


# will be the abstract controller class
class Controller(object):
    """Uses the game information to determine playcall."""

    def getPlayCall(self, game):
         raise NotImplementedError('abstract')


# This class should probably be in its own file
class AskMadden(Controller):
    """Ask Madden controller."""

    def getPlayCall(self, game):
        playName = "Ask Madden"
        formNum = None
        setNum = None
        button = None
        number = None
        flip = None
        return playName, formNum, setNum, button, number, flip


class randomPlay(Controller):
    """Random play call controller."""

    def getPlayCall(self, gameState):
        # need some logic for 4th downs
        try:
            play = dfOffPlaybook.loc[randint(0, 65)] if gameState['HomeOnOff'] else dfDefPlaybook.loc[randint(0, 41)]

            button = play.Button
            setNum = play.SetNum
            formNum = play.FormNum
            if gameState['down'] == 4 or gameState['down'] == -1 or gameState['down'] == 5:
                playName = "Ask Madden"
            else:
                playName = play.Name
            number = play.Number
        except:
            play = dfDefPlaybook.loc[randint(0, 42)]

            button = play.Button
            setNum = play.SetNum
            formNum = play.FormNum
            playName = play.Name
            number = play.Number

        flip = None

        return playName, formNum, setNum, button, number, flip

class randomTexan(Controller):
    """Random play call controller."""

    def getPlayCall(self, gameState):

        if gameState['HomeOnOff']:
            play = dfTexanPlaybook.loc[randint(0, 25)]
            button = "A"
            setNum = play.SetNum
            formNum = play.FormNum
            playName = "Texan"
            flip = randint(0,1)
            number = None
        else:
            play = dfDefPlaybook.loc[randint(0, 42)]

            button = play.Button
            setNum = play.SetNum
            formNum = play.FormNum
            playName = play.Name
            number = play.Number
            flip = None

        return playName, formNum, setNum, button, number, flip

class randomColt(Controller):
    """Random play call controller."""

    def getPlayCall(self, gameState):

        if gameState['HomeOnOff']:
            play = dfColtPlaybook.loc[randint(0, 30)]
            button = "A"
            setNum = play.SetNum
            formNum = play.FormNum
            playName = "Texan"
            flip = randint(0,1)
            number = None
        else:
            play = dfDefPlaybook.loc[randint(0, 42)]

            button = play.Button
            setNum = play.SetNum
            formNum = play.FormNum
            playName = play.Name
            number = play.Number
            flip = None

        return playName, formNum, setNum, button, number, flip
