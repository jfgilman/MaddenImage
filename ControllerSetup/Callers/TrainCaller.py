import Caller as C
import pandas as pd
import numpy as np
from sklearn import preprocessing
import sys
import time

def getTargets(data):

    off_RFENP = C.RFENP("ControllerSetup/Callers/Models/off_RFENP.sav", "ControllerSetup/Callers/Models/off_RFWP.sav", "offense")
    def_RFENP = C.RFENP("ControllerSetup/Callers/Models/def_RFENP.sav", "ControllerSetup/Callers/Models/def_RFWP.sav", "defense")

    off_RFENP.load()
    def_RFENP.load()

    std_scaleENP = preprocessing.StandardScaler().fit(data[['Change_EP']])
    std_scaleWP = preprocessing.StandardScaler().fit(data[['Change_WP']])

    targets = np.zeros(len(data))
    include = np.zeros(len(data), dtype=bool)
    for i in range(len(data) - 1):
        if data['half'].values[i] == data['half'].values[i+1] and data['secs'].values[i+1] > 0:
            include[i] = True
        else:
            include[i] = False
        if data['half'].values[i] == 0:
            value = std_scaleENP.transform(data['Change_EP'].values[i])
        else:
            value = std_scaleWP.transform(data['Change_WP'].values[i])

        if data['homeBall'].values[i+1] == 1:
            state = np.zeros(10)
            state[0] = data['scoreDif'].values[i+1]
            state[1] = data['half'].values[i+1]
            state[2] = data['secs'].values[i+1]
            state[3] = data['firstDown'].values[i+1]
            state[4] = data['secondDown'].values[i+1]
            state[5] = data['thirdDown'].values[i+1]
            state[6] = data['distance'].values[i+1]
            state[7] = data['YTEZ'].values[i+1]
            state[8] = data['raiders'].values[i+1]
            state[9] = data['broncos'].values[i+1]

            Qvalues = off_RFENP.getValues(np.reshape(state, (1, -1)))

            targets[i] = value + np.argmax(Qvalues)
        else:
            state = np.zeros(20)
            state[0] = data['scoreDif'].values[i+1]
            state[1] = data['half'].values[i+1]
            state[2] = data['secs'].values[i+1]
            state[3] = data['firstDown'].values[i+1]
            state[4] = data['secondDown'].values[i+1]
            state[5] = data['thirdDown'].values[i+1]
            state[6] = data['distance'].values[i+1]
            state[7] = data['YTEZ'].values[i+1]
            state[8] = data['raiders'].values[i+1]
            state[9] = data['broncos'].values[i+1]
            state[10] = data['offPersonel_fieldgoal'].values[i+1]
            state[11] = data['offPersonel_punt'].values[i+1]
            state[12] = data['offPersonel_RB1TE0WR4'].values[i+1]
            state[13] = data['offPersonel_RB1TE1WR3'].values[i+1]
            state[14] = data['offPersonel_RB1TE2WR2'].values[i+1]
            state[15] = data['offPersonel_RB1TE3WR1'].values[i+1]
            state[16] = data['offPersonel_RB2TE0WR3'].values[i+1]
            state[17] = data['offPersonel_RB2TE1WR2'].values[i+1]
            state[18] = data['offPersonel_RB2TE2WR1'].values[i+1]
            state[19] = data['offPersonel_RB2TE3WR0'].values[i+1]

            Qvalues = def_RFENP.getValues(np.reshape(state, (1, -1)))

            targets[i] = value + np.argmax(Qvalues)

        if i % 1000 == 0:
            print(str(i) + " of " + str(len(data)))

    return(targets, include)

t = time.time()
mData = pd.read_csv("data/cleanData.csv")

# mData = mData.head(10000)

plays = pd.get_dummies(mData, columns = ['offPersonel'])

plays = plays[np.isfinite(plays['Change_EP'])]
plays = plays.reset_index(drop=True)

plays = plays[np.isfinite(plays['Change_WP'])]
plays = plays.reset_index(drop=True)
t0 = time.time()
print("data loaded")
print('load time:' + str(t0 - t))


if sys.argv[1] == "RF":
    off_RFENP = C.RFENP("ControllerSetup/Callers/Models/off_RFENP.sav", "ControllerSetup/Callers/Models/off_RFWP.sav", "offense")
    def_RFENP = C.RFENP("ControllerSetup/Callers/Models/def_RFENP.sav", "ControllerSetup/Callers/Models/def_RFWP.sav", "defense")

    off_RFENP.fit(plays)
    def_RFENP.fit(plays)

if sys.argv[1] == "RFQ1":

    t1 = time.time()
    targets, plays['include'] = getTargets(plays)
    t2 = time.time()
    print("targets done")
    print('targets time:' + str(t2 - t1))

    # train RFQ1
    off_RFQ1 = C.RFQ1("ControllerSetup/Callers/Models/off_RFQ1.sav", mType="offense")
    def_RFQ1 = C.RFQ1("ControllerSetup/Callers/Models/def_RFQ1.sav", mType="defense")

    # not ready
    off_RFQ1.fit(plays, targets)
    def_RFQ1.fit(plays, targets)

    print("Models fit")



state = np.zeros(10)
state[2] = 300
state[3] = 1
state[6] = 10
state[7] = 45

off_RFQ1 = C.RFQ1("ControllerSetup/Callers/Models/off_RFQ1.sav", mType="offense")

off_RFQ1.load()

print(off_RFQ1.getValues(np.reshape(state, (1, -1))))
