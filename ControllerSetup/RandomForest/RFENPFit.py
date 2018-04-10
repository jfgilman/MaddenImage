from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import numpy as np
import pickle

mData = pd.read_csv("data/cleanData.csv")

plays = pd.get_dummies(mData, columns = ['offPersonel'])

plays = plays[np.isfinite(plays['Change_EP'])]

plays = plays.reset_index(drop=True)

off_features = ['scoreDif', 'half', 'secs', 'firstDown', 'secondDown',
                'thirdDown', 'distance', 'YTEZ', 'raiders', 'broncos']
def_features = ['scoreDif', 'half', 'secs', 'firstDown', 'secondDown',
                'thirdDown', 'distance', 'YTEZ', 'raiders', 'broncos',
                'offPersonel_fieldgoal', 'offPersonel_punt', 'offPersonel_RB1TE0WR4',
                'offPersonel_RB1TE1WR3', 'offPersonel_RB1TE2WR2', 'offPersonel_RB1TE3WR1',
                'offPersonel_RB2TE0WR3', 'offPersonel_RB2TE1WR2', 'offPersonel_RB2TE2WR1',
                'offPersonel_RB2TE3WR0']

offModelList = []
for i in range(1, 67):
    play = plays[plays['Play_Num'] == i]

    y = play['Change_EP']
    X = play[off_features]
    regr_rf = RandomForestRegressor(max_depth=20, random_state=2)

    offModelList.append(regr_rf.fit(X, y))

defModelList = []
for i in range(78, 120):
    play = plays[plays['Play_Num'] == i]

    y = play['Change_EP']
    X = play[def_features]
    regr_rf = RandomForestRegressor(max_depth=20, random_state=2)

    defModelList.append(regr_rf.fit(X, y))

ls = list(range(1, 67))
ls.append(68)
ls.append(71)

fourthModelList = []
for i in ls:
    play = plays[plays['Play_Num'] == i]

    y = play['Change_EP']
    X = play[off_features]
    regr_rf = RandomForestRegressor(max_depth=20, random_state=2)

    fourthModelList.append(regr_rf.fit(X, y))

offfilename = 'ControllerSetup/RandomForest/offense_RFENP_models.sav'
pickle.dump(offModelList, open(offfilename, 'wb'))

deffilename = 'ControllerSetup/RandomForest/defense_RFENP_models.sav'
pickle.dump(defModelList, open(deffilename, 'wb'))

fourthfilename = 'ControllerSetup/RandomForest/fourth_RFENP_models.sav'
pickle.dump(fourthModelList, open(fourthfilename, 'wb'))
