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

loaded_off_RF_model = pickle.load(open("C:/Temp/Madden/ControllerSetup/RandomForest/offense_RF_models.sav", 'rb'))
loaded_def_RF_model = pickle.load(open("C:/Temp/Madden/ControllerSetup/RandomForest/defense_RF_models.sav", 'rb'))

loaded_off_RFENP_model = pickle.load(open("C:/Temp/Madden/ControllerSetup/RandomForest/offense_RFENP_models.sav", 'rb'))
loaded_def_RFENP_model = pickle.load(open("C:/Temp/Madden/ControllerSetup/RandomForest/defense_RFENP_models.sav", 'rb'))
loaded_fourth_RFENP_model = pickle.load(open("C:/Temp/Madden/ControllerSetup/RandomForest/fourth_RFENP_models.sav", 'rb'))

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
        return playName, formNum, setNum, button, number


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

        return playName, formNum, setNum, button, number


class RFExplorePlay(Controller):

    def __init__(self, homeTeam, awayTeam, quarterLength):
        self.homeTeam = homeTeam
        self.awayTeam = awayTeam
        self.quarterLength = quarterLength

    def getPlayCall(self, gameState):

        playName = None
        formNum = None
        setNum = None
        button = None
        number = None

        if gameState['down'] == 5 and gameState['HomeOnOff']:
            if goForTwoAgg(gameState['homeScore'], gameState['awayScore'], gameState['quarter'], gameState['secsLeft'], self.quarterLength):
                state = np.zeros(10)
                state[0] = -7
                state[2] = 300
                state[5] = 1
                state[6] = 2
                state[7] = 2
                state[9] = 1 if self.awayTeam == "broncos" else 0
                state[8] = 1 if self.awayTeam == "raiders" else 0

                muHats = np.concatenate([mod.predict(np.reshape(state, (1, -1))) for mod in loaded_off_RF_model], axis=0)
                playLoc = np.argmax(muHats)
                setNum = dfOffPlaybook['SetNum'][playLoc]
                button = dfOffPlaybook['Button'][playLoc]
                number = dfOffPlaybook['Number'][playLoc]
                formNum = dfOffPlaybook['FormNum'][playLoc]
            else:
                playName = 'FG'
                number = 68
                button = 'X'
                formNum = 9
                setNum = 1
        elif gameState['down'] == -1 or gameState['down'] == 5:
            playName = "Ask Madden"
        elif gameState['HomeOnOff']:
            if takeKnee(gameState):
                setNum = 9
                button = 'Y'
                number = 76
                formNum = 4
            elif gameState['down'] != 4:
                # set up state vector
                state = np.zeros(10)
                # Score dif
                state[0] = gameState['homeScore'] - gameState['awayScore']
                # half
                state[1] = 1 if gameState['quarter'] < 3 else 0
                # seconds left in the half
                state[2] = gameState['secsLeft'] * self.quarterLength if gameState['quarter'] == 1 or gameState['quarter'] == 3 else gameState['secsLeft']

                state[3] = 1 if gameState['down'] == 1 else 0
                state[4] = 1 if gameState['down'] == 2 else 0
                state[5] = 1 if gameState['down'] == 3 else 0
                # distance
                state[6] = gameState['distance']
                # yards to endzone
                state[7] = gameState['YTEZ']
                state[9] = 1 if self.awayTeam == "broncos" else 0
                state[8] = 1 if self.awayTeam == "raiders" else 0

                muHats = np.concatenate([mod.predict(np.reshape(state, (1, -1))) for mod in loaded_off_RF_model], axis=0)
                playLoc = np.argmax(muHats)
                setNum = dfOffPlaybook['SetNum'][playLoc]
                button = dfOffPlaybook['Button'][playLoc]
                number = dfOffPlaybook['Number'][playLoc]
                formNum = dfOffPlaybook['FormNum'][playLoc]
            elif gameState['down'] == 4 and randint(0, 1) == 1:
                # set up state vector
                state = np.zeros(10)
                # Score dif
                state[0] = gameState['homeScore'] - gameState['awayScore']
                # half
                state[1] = 1 if gameState['quarter'] < 3 else 0
                # seconds left in the half
                state[2] = gameState['secsLeft'] * self.quarterLength if gameState['quarter'] == 1 or gameState['quarter'] == 3 else gameState['secsLeft']
                # distance
                state[6] = gameState['distance']
                # yards to endzone
                state[7] = gameState['YTEZ']
                state[9] = 1 if self.awayTeam == "broncos" else 0
                state[8] = 1 if self.awayTeam == "raiders" else 0

                muHats = np.concatenate([mod.predict(np.reshape(state, (1, -1))) for mod in loaded_off_RF_model], axis=0)
                playLoc = np.argmax(muHats)
                setNum = dfOffPlaybook['SetNum'][playLoc]
                button = dfOffPlaybook['Button'][playLoc]
                number = dfOffPlaybook['Number'][playLoc]
                formNum = dfOffPlaybook['FormNum'][playLoc]
            else:
                playName = "Ask Madden"
        else:
            if gameState['down'] == 4:
                playName = "Ask Madden"
            else:
                # set up state vector
                state = np.zeros(20)
                # Score dif
                state[0] = gameState['homeScore'] - gameState['awayScore']
                # half
                if gameState['quarter'] < 3:
                    state[1] = 1
                # seconds left in the half
                state[2] = gameState['secsLeft'] * self.quarterLength if gameState['quarter'] == 1 or gameState['quarter'] == 3 else gameState['secsLeft']
                # down
                state[3] = 1 if gameState['down'] == 1 else 0
                state[4] = 1 if gameState['down'] == 2 else 0
                state[5] = 1 if gameState['down'] == 3 else 0

                if state[2] < 10:
                    state[3] = 0
                    state[4] = 0
                    state[5] = 0
                # distance
                state[6] = gameState['distance']
                # yards to endzone
                state[7] = gameState['YTEZ']
                state[9] = 1 if self.awayTeam == "broncos" else 0
                state[8] = 1 if self.awayTeam == "raiders" else 0

                state[10] = 1 if gameState['offPersonel'] == "fieldgoal" else 0
                state[11] = 1 if gameState['offPersonel'] == "punt" else 0
                state[12] = 1 if gameState['offPersonel'] == "RB1TE0WR4" else 0
                state[13] = 1 if gameState['offPersonel'] == "RB1TE1WR3" else 0
                state[14] = 1 if gameState['offPersonel'] == "RB1TE2WR2" else 0
                state[15] = 1 if gameState['offPersonel'] == "RB1TE3WR1" else 0
                state[16] = 1 if gameState['offPersonel'] == "RB2TE0WR3" else 0
                state[17] = 1 if gameState['offPersonel'] == "RB2TE1WR2" else 0
                state[18] = 1 if gameState['offPersonel'] == "RB2TE2WR1" else 0
                state[19] = 1 if gameState['offPersonel'] == "RB2TE3WR0" else 0

                muHats = np.concatenate([mod.predict(np.reshape(state, (1, -1))) for mod in loaded_def_RF_model], axis=0)
                playLoc = np.argmax(muHats)
                setNum = dfDefPlaybook['SetNum'][playLoc]
                button = dfDefPlaybook['Button'][playLoc]
                number = dfDefPlaybook['Number'][playLoc]
                formNum = dfDefPlaybook['FormNum'][playLoc]

        return playName, formNum, setNum, button, number

class RFPlay(Controller):
    """Random Forest greedy play call controller."""

    def __init__(self, homeTeam, awayTeam, quarterLength):
        self.homeTeam = homeTeam
        self.awayTeam = awayTeam
        self.quarterLength = quarterLength

    def getPlayCall(self, gameState):

        playName = None
        formNum = None
        setNum = None
        button = None
        number = None

        if gameState['down'] == 5 and gameState['HomeOnOff']:
            if goForTwoAgg(gameState['homeScore'], gameState['awayScore'], gameState['quarter'], gameState['secsLeft'], self.quarterLength):
                state = np.zeros(10)
                state[0] = -7
                state[2] = 300
                state[5] = 1
                state[6] = 2
                state[7] = 2
                state[9] = 1 if self.awayTeam == "broncos" else 0
                state[8] = 1 if self.awayTeam == "raiders" else 0

                muHats = np.concatenate([mod.predict(np.reshape(state, (1, -1))) for mod in loaded_off_RF_model], axis=0)
                playLoc = np.argmax(muHats)
                playName = str(dfOffPlaybook['Name'][playLoc])
                print(playName)
                print("Test 2pc:", dfOffPlaybook['Name'][playLoc])
                setNum = dfOffPlaybook['SetNum'][playLoc]
                button = dfOffPlaybook['Button'][playLoc]
                number = dfOffPlaybook['Number'][playLoc]
                formNum = dfOffPlaybook['FormNum'][playLoc]
            else:
                playName = 'FG'
                number = 68
                button = 'X'
                formNum = 9
                setNum = 1
        elif gameState['down'] == -1 or gameState['down'] == 5:
            playName = "Ask Madden"
            # Evaluate regression models on current state for offensive plays
        elif gameState['HomeOnOff']:
            if takeKnee(gameState):
                setNum = 9
                button = 'Y'
                number = 76
                formNum = 4
            else:
                # set up state vector
                state = np.zeros(10)
                # Score dif
                state[0] = gameState['homeScore'] - gameState['awayScore']
                # half
                state[1] = 1 if gameState['quarter'] < 3 else 0
                # seconds left in the half
                state[2] = gameState['secsLeft'] * self.quarterLength if gameState['quarter'] == 1 or gameState['quarter'] == 3 else gameState['secsLeft']
                # down
                state[3] = 1 if gameState['down'] == 1 else 0
                state[4] = 1 if gameState['down'] == 2 else 0
                state[5] = 1 if gameState['down'] == 3 else 0
                # treat late half as 4th down
                if state[2] < 10:
                    state[3] = 0
                    state[4] = 0
                    state[5] = 0
                # distance
                state[6] = gameState['distance']
                # yards to endzone
                state[7] = gameState['YTEZ']
                state[9] = 1 if self.awayTeam == "broncos" else 0
                state[8] = 1 if self.awayTeam == "raiders" else 0

                muHats = np.concatenate([mod.predict(np.reshape(state, (1, -1))) for mod in loaded_off_RF_model], axis=0)
                playLoc = np.argmax(muHats)
                playName = str(dfOffPlaybook['Name'][playLoc])
                print(playName)
                print("Test Off:", dfOffPlaybook['Name'][playLoc])
                setNum = dfOffPlaybook['SetNum'][playLoc]
                button = dfOffPlaybook['Button'][playLoc]
                number = dfOffPlaybook['Number'][playLoc]
                formNum = dfOffPlaybook['FormNum'][playLoc]
        else:
            # set up state vector
            state = np.zeros(20)
            # Score dif
            state[0] = gameState['homeScore'] - gameState['awayScore']
            # half
            if gameState['quarter'] < 3:
                state[1] = 1
            # seconds left in the half
            state[2] = gameState['secsLeft'] * self.quarterLength if gameState['quarter'] == 1 or gameState['quarter'] == 3 else gameState['secsLeft']
            # down
            state[3] = 1 if gameState['down'] == 1 else 0
            state[4] = 1 if gameState['down'] == 2 else 0
            state[5] = 1 if gameState['down'] == 3 else 0

            if state[2] < 10:
                state[3] = 0
                state[4] = 0
                state[5] = 0
            # distance
            state[6] = gameState['distance']
            # yards to endzone
            state[7] = gameState['YTEZ']
            state[9] = 1 if self.awayTeam == "broncos" else 0
            state[8] = 1 if self.awayTeam == "raiders" else 0

            state[10] = 1 if gameState['offPersonel'] == "fieldgoal" else 0
            state[11] = 1 if gameState['offPersonel'] == "punt" else 0
            state[12] = 1 if gameState['offPersonel'] == "RB1TE0WR4" else 0
            state[13] = 1 if gameState['offPersonel'] == "RB1TE1WR3" else 0
            state[14] = 1 if gameState['offPersonel'] == "RB1TE2WR2" else 0
            state[15] = 1 if gameState['offPersonel'] == "RB1TE3WR1" else 0
            state[16] = 1 if gameState['offPersonel'] == "RB2TE0WR3" else 0
            state[17] = 1 if gameState['offPersonel'] == "RB2TE1WR2" else 0
            state[18] = 1 if gameState['offPersonel'] == "RB2TE2WR1" else 0
            state[19] = 1 if gameState['offPersonel'] == "RB2TE3WR0" else 0

            muHats = np.concatenate([mod.predict(np.reshape(state, (1, -1))) for mod in loaded_def_RF_model], axis=0)
            playLoc = np.argmax(muHats)
            setNum = dfDefPlaybook['SetNum'][playLoc]
            button = dfDefPlaybook['Button'][playLoc]
            number = dfDefPlaybook['Number'][playLoc]
            formNum = dfDefPlaybook['FormNum'][playLoc]
            playName = str(dfDefPlaybook['Name'][playLoc])
            print(playName)
            print("Test def:", dfDeffPlaybook['Name'][playLoc])

        return playName, formNum, setNum, button, number

class RFENPGoForIt(Controller):

    def __init__(self, homeTeam, awayTeam, quarterLength):
        self.homeTeam = homeTeam
        self.awayTeam = awayTeam
        self.quarterLength = quarterLength

    def getPlayCall(self, gameState):

        playName = None
        formNum = None
        setNum = None
        button = None
        number = None

        if gameState['down'] == 5 and gameState['HomeOnOff']:
            if goForTwoAgg(gameState['homeScore'], gameState['awayScore'], gameState['quarter'], gameState['secsLeft'], self.quarterLength):
                possible_plays = [25, 15, 34]
                play = dfOffPlaybook.loc[choice(possible_plays)]

                button = play.Button
                setNum = play.SetNum
                formNum = play.FormNum
                playName = play.Name
                number = play.Number
            else:
                playName = 'FG'
                number = 68
                button = 'X'
                formNum = 9
                setNum = 1
            # Replace randint with random integer from a set
        elif gameState['down'] == -1 or gameState['down'] == 5:
            playName = "Ask Madden"
        elif gameState['HomeOnOff']:
            if takeKnee(gameState):
                setNum = 9
                button = 'Y'
                number = 76
                formNum = 4
            elif gameState['down'] != 4:
                # set up state vector
                state = np.zeros(10)
                # Score dif
                state[0] = gameState['homeScore'] - gameState['awayScore']
                # half
                state[1] = 1 if gameState['quarter'] < 3 else 0
                # seconds left in the half
                state[2] = gameState['secsLeft'] * self.quarterLength if gameState['quarter'] == 1 or gameState['quarter'] == 3 else gameState['secsLeft']

                state[3] = 1 if gameState['down'] == 1 else 0
                state[4] = 1 if gameState['down'] == 2 else 0
                state[5] = 1 if gameState['down'] == 3 else 0
                # distance
                state[6] = gameState['distance']
                # yards to endzone
                state[7] = gameState['YTEZ']
                state[9] = 1 if self.awayTeam == "broncos" else 0
                state[8] = 1 if self.awayTeam == "raiders" else 0

                muHats = np.concatenate([mod.predict(np.reshape(state, (1, -1))) for mod in loaded_off_RFENP_model], axis=0)
                playLoc = choice(list(range(0, 66)), p=softmax(muHats))
                playName = str(dfOffPlaybook['Name'][playLoc])
                setNum = dfOffPlaybook['SetNum'][playLoc]
                button = dfOffPlaybook['Button'][playLoc]
                number = dfOffPlaybook['Number'][playLoc]
                formNum = dfOffPlaybook['FormNum'][playLoc]
            elif gameState['down'] == 4:
                playLoc = choice(list(range(0, 66)))
                playName = str(dfOffPlaybook['Name'][playLoc])
                setNum = dfOffPlaybook['SetNum'][playLoc]
                button = dfOffPlaybook['Button'][playLoc]
                number = dfOffPlaybook['Number'][playLoc]
                formNum = dfOffPlaybook['FormNum'][playLoc]
            else:
                playName = "Ask Madden"
        else:
            if gameState['down'] == 4:
                playName = "Ask Madden"
            else:
                # set up state vector
                state = np.zeros(20)
                # Score dif
                state[0] = gameState['homeScore'] - gameState['awayScore']
                # half
                if gameState['quarter'] < 3:
                    state[1] = 1
                # seconds left in the half
                state[2] = gameState['secsLeft'] * self.quarterLength if gameState['quarter'] == 1 or gameState['quarter'] == 3 else gameState['secsLeft']
                # down
                state[3] = 1 if gameState['down'] == 1 else 0
                state[4] = 1 if gameState['down'] == 2 else 0
                state[5] = 1 if gameState['down'] == 3 else 0

                if state[2] < 10:
                    state[3] = 0
                    state[4] = 0
                    state[5] = 0
                # distance
                state[6] = gameState['distance']
                # yards to endzone
                state[7] = gameState['YTEZ']
                state[9] = 1 if self.awayTeam == "broncos" else 0
                state[8] = 1 if self.awayTeam == "raiders" else 0

                state[10] = 1 if gameState['offPersonel'] == "fieldgoal" else 0
                state[11] = 1 if gameState['offPersonel'] == "punt" else 0
                state[12] = 1 if gameState['offPersonel'] == "RB1TE0WR4" else 0
                state[13] = 1 if gameState['offPersonel'] == "RB1TE1WR3" else 0
                state[14] = 1 if gameState['offPersonel'] == "RB1TE2WR2" else 0
                state[15] = 1 if gameState['offPersonel'] == "RB1TE3WR1" else 0
                state[16] = 1 if gameState['offPersonel'] == "RB2TE0WR3" else 0
                state[17] = 1 if gameState['offPersonel'] == "RB2TE1WR2" else 0
                state[18] = 1 if gameState['offPersonel'] == "RB2TE2WR1" else 0
                state[19] = 1 if gameState['offPersonel'] == "RB2TE3WR0" else 0

                muHats = np.concatenate([mod.predict(np.reshape(state, (1, -1))) for mod in loaded_def_RFENP_model], axis=0)
                playLoc = choice(list(range(0, 42)), p=softmax(muHats))
                playName = str(dfDefPlaybook['Name'][playLoc])
                setNum = dfDefPlaybook['SetNum'][playLoc]
                button = dfDefPlaybook['Button'][playLoc]
                number = dfDefPlaybook['Number'][playLoc]
                formNum = dfDefPlaybook['FormNum'][playLoc]

        return playName, formNum, setNum, button, number


class RFENPExplore(Controller):

    def __init__(self, homeTeam, awayTeam, quarterLength):
        self.homeTeam = homeTeam
        self.awayTeam = awayTeam
        self.quarterLength = quarterLength

    def getPlayCall(self, gameState):

        playName = None
        formNum = None
        setNum = None
        button = None
        number = None

        if gameState['down'] == 5 and gameState['HomeOnOff']:
            if goForTwoAgg(gameState['homeScore'], gameState['awayScore'], gameState['quarter'], gameState['secsLeft'], self.quarterLength):
                possible_plays = [25, 15, 34]
                play = dfOffPlaybook.loc[choice(possible_plays)]

                button = play.Button
                setNum = play.SetNum
                formNum = play.FormNum
                playName = play.Name
                number = play.Number
            else:
                playName = 'FG'
                number = 68
                button = 'X'
                formNum = 9
                setNum = 1
            # Replace randint with random integer from a set
        elif gameState['down'] == -1 or gameState['down'] == 5:
            playName = "Ask Madden"
        elif gameState['HomeOnOff']:
            if takeKnee(gameState):
                setNum = 9
                button = 'Y'
                number = 76
                formNum = 4
            elif gameState['down'] != 4:
                # set up state vector
                state = np.zeros(10)
                # Score dif
                state[0] = gameState['homeScore'] - gameState['awayScore']
                # half
                state[1] = 1 if gameState['quarter'] < 3 else 0
                # seconds left in the half
                state[2] = gameState['secsLeft'] * self.quarterLength if gameState['quarter'] == 1 or gameState['quarter'] == 3 else gameState['secsLeft']

                state[3] = 1 if gameState['down'] == 1 else 0
                state[4] = 1 if gameState['down'] == 2 else 0
                state[5] = 1 if gameState['down'] == 3 else 0
                # distance
                state[6] = gameState['distance']
                # yards to endzone
                state[7] = gameState['YTEZ']
                state[9] = 1 if self.awayTeam == "broncos" else 0
                state[8] = 1 if self.awayTeam == "raiders" else 0

                muHats = np.concatenate([mod.predict(np.reshape(state, (1, -1))) for mod in loaded_off_RFENP_model], axis=0)
                playLoc = choice(list(range(0, 66)), p=softmax(muHats))
                playName = str(dfOffPlaybook['Name'][playLoc])
                setNum = dfOffPlaybook['SetNum'][playLoc]
                button = dfOffPlaybook['Button'][playLoc]
                number = dfOffPlaybook['Number'][playLoc]
                formNum = dfOffPlaybook['FormNum'][playLoc]
            elif gameState['down'] == 4:
                # set up state vector
                state = np.zeros(10)
                # Score dif
                state[0] = gameState['homeScore'] - gameState['awayScore']
                # half
                state[1] = 1 if gameState['quarter'] < 3 else 0
                # seconds left in the half
                state[2] = gameState['secsLeft'] * self.quarterLength if gameState['quarter'] == 1 or gameState['quarter'] == 3 else gameState['secsLeft']
                # distance
                state[6] = gameState['distance']
                # yards to endzone
                state[7] = gameState['YTEZ']
                state[8] = 1 if self.awayTeam == "raiders" else 0
                state[9] = 1 if self.awayTeam == "broncos" else 0

                muHats = np.concatenate([mod.predict(np.reshape(state, (1, -1))) for mod in loaded_fourth_RFENP_model], axis=0)
                ls = list(range(1, 67))
                ls.append(68)
                ls.append(71)
                playLoc = choice(ls, p=softmax(muHats))
                playName = str(dfOffPlaybook['Name'][playLoc])
                setNum = dfOffPlaybook['SetNum'][playLoc]
                button = dfOffPlaybook['Button'][playLoc]
                number = dfOffPlaybook['Number'][playLoc]
                formNum = dfOffPlaybook['FormNum'][playLoc]
            else:
                playName = "Ask Madden"
        else:
            if gameState['down'] == 4:
                playName = "Ask Madden"
            else:
                # set up state vector
                state = np.zeros(20)
                # Score dif
                state[0] = gameState['homeScore'] - gameState['awayScore']
                # half
                if gameState['quarter'] < 3:
                    state[1] = 1
                # seconds left in the half
                state[2] = gameState['secsLeft'] * self.quarterLength if gameState['quarter'] == 1 or gameState['quarter'] == 3 else gameState['secsLeft']
                # down
                state[3] = 1 if gameState['down'] == 1 else 0
                state[4] = 1 if gameState['down'] == 2 else 0
                state[5] = 1 if gameState['down'] == 3 else 0

                if state[2] < 10:
                    state[3] = 0
                    state[4] = 0
                    state[5] = 0
                # distance
                state[6] = gameState['distance']
                # yards to endzone
                state[7] = gameState['YTEZ']
                state[9] = 1 if self.awayTeam == "broncos" else 0
                state[8] = 1 if self.awayTeam == "raiders" else 0

                state[10] = 1 if gameState['offPersonel'] == "fieldgoal" else 0
                state[11] = 1 if gameState['offPersonel'] == "punt" else 0
                state[12] = 1 if gameState['offPersonel'] == "RB1TE0WR4" else 0
                state[13] = 1 if gameState['offPersonel'] == "RB1TE1WR3" else 0
                state[14] = 1 if gameState['offPersonel'] == "RB1TE2WR2" else 0
                state[15] = 1 if gameState['offPersonel'] == "RB1TE3WR1" else 0
                state[16] = 1 if gameState['offPersonel'] == "RB2TE0WR3" else 0
                state[17] = 1 if gameState['offPersonel'] == "RB2TE1WR2" else 0
                state[18] = 1 if gameState['offPersonel'] == "RB2TE2WR1" else 0
                state[19] = 1 if gameState['offPersonel'] == "RB2TE3WR0" else 0

                muHats = np.concatenate([mod.predict(np.reshape(state, (1, -1))) for mod in loaded_def_RFENP_model], axis=0)
                playLoc = choice(list(range(0, 42)), p=softmax(muHats))
                playName = str(dfDefPlaybook['Name'][playLoc])
                setNum = dfDefPlaybook['SetNum'][playLoc]
                button = dfDefPlaybook['Button'][playLoc]
                number = dfDefPlaybook['Number'][playLoc]
                formNum = dfDefPlaybook['FormNum'][playLoc]

        return playName, formNum, setNum, button, number


def softmax(X, theta=1000, axis=1):
    """
    Compute the softmax of each element along an axis of X.

    Returns: An array the same size as X. The result will sum to 1
        along the specified axis.

    """
    y = np.atleast_2d(X)
    if axis is None:
        axis = next(j[0] for j in enumerate(y.shape) if j[1] > 1)
    y = y * float(theta)
    y = y - np.expand_dims(np.max(y, axis=axis), axis)
    y = np.exp(y)
    ax_sum = np.expand_dims(np.sum(y, axis=axis), axis)
    p = y / ax_sum
    if len(X.shape) == 1:
        p = p.flatten()
    return p

def takeKnee(gameState):
    if gameState['HomeOnOff'] and gameState['AwayTOR'] == 0 and gameState['YTEZ'] < 97 and gameState['quarter'] == 4 and gameState['homeScore'] > gameState['awayScore']:
        if gameState['down'] == 1 and gameState['secsLeft'] < 65:
            return True
        elif  gameState['down'] == 2 and gameState['secsLeft'] < 45:
            return True
        elif gameState['down'] == 3 and gameState['secsLeft'] < 25:
            return True
        else:
            return False
    else:
        return False
