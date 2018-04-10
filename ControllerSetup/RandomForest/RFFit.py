from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import numpy as np
import pickle

plays = pd.read_csv("ControllerSetup/MCTSRegression/playData.csv")

offFeatures = np.concatenate([plays.columns[4:12], plays.columns[21:23]])
defFeatures = np.concatenate([plays.columns[4:12], plays.columns[21:33]])

offModelList = []
for i in range(1, 67):
    play = plays[plays['Play_Num'] == i]
    play = play[play.Change_In_WP < 1E308]

    X = play[offFeatures]
    y = play['Change_In_WP']
    regr_rf = RandomForestRegressor(max_depth=20, random_state=2)

    offModelList.append(regr_rf.fit(X, y))

defModelList = []
for i in range(78, 120):
    play = plays[plays['Play_Num'] == i]
    play = play[play.Change_In_WP < 1E308]

    X = play[defFeatures]
    y = play['Change_In_WP']
    regr_rf = RandomForestRegressor(max_depth=20, random_state=2)

    defModelList.append(regr_rf.fit(X, y))

offfilename = 'Controller/RandomForest/offense_RF_models.sav'
pickle.dump(offModelList, open(offfilename, 'wb'))

deffilename = 'Controller/RandomForest/defense_RF_models.sav'
pickle.dump(defModelList, open(deffilename, 'wb'))
