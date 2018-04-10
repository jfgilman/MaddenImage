from sklearn.ensemble import RandomForestRegressor
from sklearn import preprocessing
import pandas as pd
import numpy as np
import pickle


# will be the abstract caller class
class Caller(object):
    """Uses the game information to determine playcall."""
    def __init__(self, ENPSaveFile, WPSaveFile=None, mType="offense"):
        self.ENPSaveFile = ENPSaveFile
        self.WPSaveFile = WPSaveFile
        self.mType = mType

    def getWeight(self, half, secs):
        # if half == 0:
        #     return 0
        # else:
        #     return (960 - secs) / 960
        if half == 0:
            return 0
        else:
            return 1


class RFENP(Caller):

    def fit(self, data):
        ENPModelList = []
        WPModelList = []
        std_scaleENP = preprocessing.StandardScaler().fit(data[['Change_EP']])
        std_scaleWP = preprocessing.StandardScaler().fit(data[['Change_WP']])
        if self.mType == "offense":
            off_features = ['scoreDif', 'half', 'secs', 'firstDown', 'secondDown',
                            'thirdDown', 'distance', 'YTEZ', 'raiders', 'broncos']
            ls = list(range(1, 67))
            ls.append(68)
            ls.append(71)

            for i in ls:
                play = data[data['Play_Num'] == i]
                cENP = std_scaleENP.transform(play[['Change_EP']])
                cWP = std_scaleWP.transform(play[['Change_WP']])
                X = play[off_features]
                regr_rf = RandomForestRegressor(max_depth=20, random_state=2)
                ENPModelList.append(regr_rf.fit(X, np.ravel(cENP)))
                WPModelList.append(regr_rf.fit(X, np.ravel(cWP)))

        elif self.mType == "defense":
            def_features = ['scoreDif', 'half', 'secs', 'firstDown', 'secondDown',
                            'thirdDown', 'distance', 'YTEZ', 'raiders', 'broncos',
                            'offPersonel_fieldgoal', 'offPersonel_punt', 'offPersonel_RB1TE0WR4',
                            'offPersonel_RB1TE1WR3', 'offPersonel_RB1TE2WR2', 'offPersonel_RB1TE3WR1',
                            'offPersonel_RB2TE0WR3', 'offPersonel_RB2TE1WR2', 'offPersonel_RB2TE2WR1',
                            'offPersonel_RB2TE3WR0']

            for i in range(78, 120):
                play = data[data['Play_Num'] == i]
                cENP = std_scaleENP.transform(play[['Change_EP']])
                cWP = std_scaleWP.transform(play[['Change_WP']])
                X = play[def_features]
                regr_rf = RandomForestRegressor(max_depth=20, random_state=2)
                ENPModelList.append(regr_rf.fit(X, np.ravel(cENP)))
                WPModelList.append(regr_rf.fit(X, np.ravel(cWP)))

        pickle.dump(ENPModelList, open(self.ENPSaveFile, 'wb'))
        pickle.dump(WPModelList, open(self.WPSaveFile, 'wb'))

    def load(self):
        self.ENPModelList = pickle.load(open(self.ENPSaveFile, 'rb'))
        self.WPModelList = pickle.load(open(self.WPSaveFile, 'rb'))

    def getValues(self, state):
        ENPmuHats = np.concatenate([mod.predict(state) for mod in self.ENPModelList], axis=0)
        WPmuHats = np.concatenate([mod.predict(state) for mod in self.WPModelList], axis=0)

        w = self.getWeight(state[0,1], state[0,2])

        return (1-w)*ENPmuHats + w*WPmuHats

class RFQ1(Caller):

    def fit(self, data, targets):
        ModelList = []
        if self.mType == "offense":
            off_features = ['scoreDif', 'half', 'secs', 'firstDown', 'secondDown',
                            'thirdDown', 'distance', 'YTEZ', 'raiders', 'broncos']
            ls = list(range(1, 67))
            ls.append(68)
            ls.append(71)

            for i in ls:
                ind = (data['Play_Num'] == i) & (data['include'])
                play = data[ind]
                X = play[off_features]
                Y = targets[ind]
                regr_rf = RandomForestRegressor(max_depth=20, random_state=2)
                ModelList.append(regr_rf.fit(X, Y))

        elif self.mType == "defense":
            def_features = ['scoreDif', 'half', 'secs', 'firstDown', 'secondDown',
                            'thirdDown', 'distance', 'YTEZ', 'raiders', 'broncos',
                            'offPersonel_fieldgoal', 'offPersonel_punt', 'offPersonel_RB1TE0WR4',
                            'offPersonel_RB1TE1WR3', 'offPersonel_RB1TE2WR2', 'offPersonel_RB1TE3WR1',
                            'offPersonel_RB2TE0WR3', 'offPersonel_RB2TE1WR2', 'offPersonel_RB2TE2WR1',
                            'offPersonel_RB2TE3WR0']

            for i in range(78, 120):
                ind = (data['Play_Num'] == i) & (data['include'])
                play = data[ind]
                X = play[def_features]
                Y = targets[ind]
                regr_rf = RandomForestRegressor(max_depth=20, random_state=2)
                ModelList.append(regr_rf.fit(X, Y))


        pickle.dump(ModelList, open(self.ENPSaveFile, 'wb'))

    def load(self):
        self.ModelList = pickle.load(open(self.ENPSaveFile, 'rb'))

    def getValues(self, state):
        muHats = np.concatenate([mod.predict(state) for mod in self.ModelList], axis=0)

        return muHats
