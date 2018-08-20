# game class
from ScreenStuff.textRecognition.getDown import getDown
from ScreenStuff.textRecognition.getDistance import getDistance
from ScreenStuff.textRecognition.getAwayScore import getAwayScore
from ScreenStuff.textRecognition.getHomeScore import getHomeScore
from ScreenStuff.textRecognition.getTime import getTime
from ScreenStuff.textRecognition.getQuarter import getQuarter
from ScreenStuff.textRecognition.getFieldPos import getFieldPos
from ScreenStuff.textRecognition.getSide import getSide
from skimage.feature import hog
from imutils import paths
from sklearn import svm
import pandas as pd
from scipy.stats import norm
import math
import cv2
import pickle
import random
import time


class Game(object):
    """
    Description of class.

    Attr:
        startTime: string
            Time the game starts
        CPUID: string
            IP adress of Raspi server
        difficulty: string
            The difficulty at which the game is played
        controllerName: string
            Name of the controller
        homeTeam: string
            Name of the home team
        awayteam: string
            Name of the away team
        gameOver: bool
            If the game is over or not
        df: DataFrame
            The data from the game being stored
        quarterLength: int
            The length of each quarter in minutes
        raitings: dictionary
            The game raitings for each team
        state: dictionary
            The current state of the game
        playCall: dictionary
            The information about the current play call for the home team
    """

    gameOver = False
    state = {'HomeOnOff': None, 'homeScore': None, 'awayScore': None, 'down': None,
             'distance': None, 'YTEZ': None, 'quarter': None, 'secsLeft': None,
             'HomeTOR': 3, 'AwayTOR': 3, 'offPersonel': None, 'winProb': None}
    playName = None
    formNum = None
    setNum = None
    button = None
    playNum = None
    timeSinceLastCall = 0
    timeOfLastCall = None
    df = pd.DataFrame(columns=['Start_Time', 'Home_Score', 'Away_Score',
                               'Home_TO_Remain', 'Away_TO_Remain', 'Quarter',
                               'Time_Remain', 'Home_Ball', 'Down', 'Distance',
                               'Yards_To_Endzone', 'Offense_Personnel',
                               'Play_Call', 'Form_Num', 'Set_Num', 'Button',
                               'Play_Num', 'Win_Prob', 'Point_Spread',
                               'Home_Team', 'Away_Team', 'Controller',
                               'CPUID', 'QuarterLength', 'Difficulty',
                               'Time_Since_Last_Call'])
    raitings = {"Bears": 75, "Bengals": 77, "Bills": 84, "broncos": 82,
                "Browns": 73, "Buccaneers": 78, "Cardinals": 86, "chargers": 80,
                "Chiefs": 88, "Colts": 81, "Cowboys": 91, "Dolphins": 83,
                "Eagles": 79, "Falcons": 90, "49ers": 74, "Giants": 84,
                "Jaguars": 76, "Jets": 73, "Lions": 81, "Packers": 89,
                "Panthers": 79, "Patriots": 93, "raiders": 85, "Rams": 72,
                "Ravens": 81, "Redskins": 82, "Saints": 84, "Seahawks": 86,
                "Steelers": 89, "Texans": 80, "Titans": 87, "Vikings": 78}
    loaded_quarter_model = pickle.load(open("ScreenStuff/svm/quarter_recog/finalized_quarter_model.sav", 'rb'))
    loaded_PAT_model = pickle.load(open("ScreenStuff/svm/PAT_recog/finalized_PAT_model.sav", 'rb'))

    def __init__(self, startTime, CPUID, difficulty, controllerName, homeTeam,
                 awayTeam, quarterLength):
        self.startTime = startTime
        self.CPUID = CPUID
        self.difficulty = difficulty
        self.controllerName = controllerName
        self.homeTeam = homeTeam
        self.awayTeam = awayTeam
        self.quarterLength = quarterLength

    @property
    def pointSpread(self):
        return self.raitings[self.homeTeam] - self.raitings[self.awayTeam]

    def updateState(self, frame):
        #self.updateQuarter(frame)
        #self.updateScore(frame)
        #self.updateField(frame)
        self.updateAwayTO(frame)

        # if self.state['YTEZ'] != -1 and self.state['distance'] != -1 and self.state['down'] != -1 and self.state['quarter'] != -1 and self.state['secsLeft'] != -1:
        #     self.updateWinProb()
        # else:
        #     self.state['winProb'] = None

    def updateOffPersonnel(self, personnel):
        self.state['offPersonel'] = personnel

    def updateScore(self, frame):
        HomeOldScore = self.state['homeScore']
        AwayOldScore = self.state['awayScore']
        quarter = self.state['quarter']
        HomeNewScore = getHomeScore(frame, self.CPUID)
        AwayNewScore = getAwayScore(frame, self.CPUID)

        try:
            if HomeOldScore is not None and (HomeNewScore == -1 or HomeNewScore > HomeOldScore + 8 or HomeNewScore < HomeOldScore) and quarter > 1:
                self.state['homeScore'] = HomeOldScore
            else:
                self.state['homeScore'] = HomeNewScore

            if AwayOldScore is not None and (AwayNewScore == -1 or AwayNewScore > AwayOldScore + 8 or AwayNewScore < AwayOldScore) and quarter > 1:
                self.state['awayScore'] = AwayOldScore
            else:
                self.state['awayScore'] = AwayNewScore
        except:
            pass

    def updateQuarter(self, frame):
        gray2 = cv2.cvtColor(frame[25:65, 710:760], cv2.COLOR_BGR2GRAY)
        fd2 = hog(gray2, orientations=8, pixels_per_cell=(8, 8), cells_per_block=(1, 1))
        quarterString = self.loaded_quarter_model.predict(fd2.reshape(1, -1))[0]
        oldQuarter = self.state['quarter']
        if quarterString == "first":
            newQuarter = 1
            self.updateHomeTimeOuts(reset = True)
        elif quarterString == "second":
            newQuarter = 2
        elif quarterString == "third":
            newQuarter = 3
            self.updateHomeTimeOuts(reset = True)
        elif quarterString == "fourth":
            newQuarter = 4
        elif quarterString == "overtime":
            newQuarter = 5
        else:
            newQuarter = -1

        if oldQuarter is not None:
            if newQuarter == 3 and oldQuarter == 4:
                self.state['quarter'] = 4
            elif newQuarter == 3 and oldQuarter == 1:
                self.state['quarter'] = 1
            else:
                self.state['quarter'] = newQuarter
        else:
            self.state['quarter'] = newQuarter

        if oldQuarter == None:
            oldQuarter = 1

        if (newQuarter == 1 and oldQuarter in [4, 5]) or (newQuarter - oldQuarter == 1):
            self.state['secsLeft'] = 480
        else:
            self.updateTime(frame)

    def updateTime(self, frame):
        oldTime = self.state['secsLeft']
        if oldTime == None:
            oldTime = 480
        timeRemaining = getTime(frame, self.CPUID)
        if timeRemaining - oldTime < -100 or timeRemaining == -1:
            self.state['secsLeft'] = oldTime - 5
        else:
            self.state['secsLeft'] = timeRemaining

    def updateField(self, frame):
        gray1 = cv2.cvtColor(frame[25:65, 250:300], cv2.COLOR_BGR2GRAY)
        fd1 = hog(gray1, orientations=8, pixels_per_cell=(16, 16), cells_per_block=(1, 1))
        PATString = self.loaded_PAT_model.predict(fd1.reshape(1, -1))[0]

        oldDist = self.state['distance']
        oldYTEZ = self.state['YTEZ']

        if PATString == "PAT":
            self.state['down'] = 5
            self.state['distance'] = 2
            self.state['YTEZ'] = 2
        else:
            down = getDown(frame, self.CPUID)
            self.state['down'] = down

            fieldPos = getFieldPos(frame, self.CPUID)
            side = getSide(frame, self.CPUID)
            if (side == "own"):
                self.state['YTEZ'] = 100 - fieldPos
            else:
                self.state['YTEZ'] = fieldPos

            if down == 1:
                if self.state['YTEZ'] > 9:
                    self.state['distance'] = 10
                else:
                    self.state['distance'] = self.state['YTEZ']
            else:
                try:
                    self.state['distance'] = oldDist - (oldYTEZ - self.state['YTEZ'])
                except:
                    self.state['distance'] = 9

        if self.state['distance'] < 0:
            path = "ScreenStuff/images/failedImages/" + self.CPUID[-3:] + "_distance_" + str(random.randint(1, 5)) + ".png"
            cv2.imwrite(path, frame)

            distance = getDistance(frame, self.CPUID)
            self.state['distance'] = distance



    def updateAwayTO(self, frame):
        TOAwayIMG = frame[27:61, 492:501]
        TOAwayIMG = cv2.cvtColor(TOAwayIMG, cv2.COLOR_RGB2GRAY)
        TOAwayVec = TOAwayIMG.flatten()
        TOAwayVecCount = sum(TOAwayVec)
        if TOAwayVecCount > 36500:
            self.state['AwayTOR'] = 3
        elif TOAwayVecCount > 32000:
            self.state['AwayTOR'] = 2
        elif TOAwayVecCount > 28000:
            self.state['AwayTOR'] = 1
        else:
            self.state['AwayTOR'] = 0

    def updateWinProb(self):
        if self.state['quarter'] < 5:
            secondsRemaining = (4 - self.state['quarter']) * self.quarterLength * 60 + self.state['secsLeft']
            totalTime = 4 * self.quarterLength * 60
            try:
                stdev = 13.86 / math.sqrt((totalTime / secondsRemaining))
            except:
                stdev = 2
        else:
            secondsRemaining = 0
            totalTime = 1
            stdev = 2

        expectedPoints = self.getExpectedPoints()
        try:
            scoreDiff = self.state['homeScore'] - self.state['awayScore']
            center = self.pointSpread * (secondsRemaining / totalTime) + expectedPoints + scoreDiff
            self.state['winProb'] = 1 - norm.cdf(0, loc=center, scale=stdev)
        except:
            pass

    def updatePlayStuff(self, playName, formNum, setNum, button, playNum):
        if self.timeOfLastCall is None:
            self.timeOfLastCall = time.time()

        self.timeSinceLastCall = time.time() - self.timeOfLastCall

        self.timeOfLastCall = time.time()

        self.playName = playName
        self.formNum = formNum
        self.setNum = setNum
        self.button = button
        self.playNum = playNum

    def updateHomeTimeOuts(self, reset=False):
        if reset:
            self.state['HomeTOR'] = 3
        else:
            self.state['HomeTOR'] = self.state['HomeTOR'] - 1

    def updateHomeBall(self, homeBall, frame, oldAwayTO):
        awayTO = self.updateAwayTO(frame)
        if (self.playNum == 71 or self.playNum == 68) and (oldAwayTO == awayTO):
            self.homeBall = False
        else:
            self.homeBall = homeBall

        self.state['HomeOnOff'] = self.homeBall

    def appendData(self):
        """
        Append pandas dataframe with current state information.

        Returns: void

        """
        rc = self.df.shape[0]
        self.df.loc[rc + 1] = [self.startTime, self.state['homeScore'],
                               self.state['awayScore'], self.state['HomeTOR'],
                               self.state['AwayTOR'], self.state['quarter'],
                               self.state['secsLeft'], self.state['HomeOnOff'],
                               self.state['down'], self.state['distance'],
                               self.state['YTEZ'], self.state['offPersonel'],
                               self.playName,
                               self.formNum,
                               self.setNum,
                               self.button,
                               self.playNum, self.state['winProb'],
                               self.pointSpread, self.homeTeam,
                               self.awayTeam, self.controllerName,
                               self.CPUID, self.quarterLength,
                               self.difficulty, self.timeSinceLastCall]

    def saveData(self, file_name):
        """
        Write a csv with the pandas dataframe.

        Returns: void

        """
        self.df.to_csv(file_name)

    def updateStateMan(self, homeBall=True, down=1, dist=10, homeScore=0,
                       awayScore=0, quarter=1, timeRemaining=480, ytez=75,
                       homeTORemaining=3, awayTORemaining=3):
        """
        Manually updates all game variables.

        Args:

        Returns: void
        """
        self.state['HomeOnOff'] = homeBall
        self.state['down'] = down
        self.state['distance'] = dist
        self.state['homeScore'] = homeScore
        self.state['awayScore'] = awayScore
        self.state['quarter'] = quarter
        self.state['secsLeft'] = timeRemaining
        self.state['YTEZ'] = ytez
        self.state['AwayTOR'] = awayTORemaining
        self.state['HomeTOR'] = homeTORemaining

        if self.state['YTEZ'] != -1 and self.state['distance'] != -1 and self.state['down'] != -1 and self.state['quarter'] != -1 and self.state['secsLeft'] != -1:
            self.updateWinProb()
        else:
            self.state['winProb'] = None

    def getExpectedPoints(self):
        """
        Gets expected points for next score.

        Returns: float
            The expected value of the next score for the home team given the
            state.

        """
        try:
            ep = 1
            if self.down == 1:
                ep = 6 - (3 / 40) * self.state['YTEZ'] - self.state['distance'] * .1
            elif self.down == 2:
                ep = 5.5 - (3 / 40) * self.state['YTEZ'] - self.state['distance'] * .1
            elif self.down == 3:
                ep = 4.5 - (3 / 40) * self.state['YTEZ'] - self.state['distance'] * .1
            elif self.down == 4:
                ep = 3.5 - (3 / 40) * self.state['YTEZ'] - self.state['distance'] * .1

            if self.homeBall:
                return ep
            else:
                return -ep
        except:
            return -1
