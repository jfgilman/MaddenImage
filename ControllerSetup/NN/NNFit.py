from keras.models import Sequential, load_model
from keras.layers.core import Dense, Activation, Dropout
import numpy as np
import pandas as pd
import time

mData = pd.read_csv("data/cleanData.csv")

plays = mData[np.isfinite(mData['Change_EP'])]

off_features = ['scoreDif', 'half', 'secs', 'firstDown', 'secondDown', 'thirdDown', 'distance', 'YTEZ', 'raiders', 'broncos']

for i in range(1, 67):
    play = plays[plays['Play_Num'] == i]

    y = play['Change_EP']
    X = play[off_features]

    model = Sequential()
    model.add(Dense(64, input_dim=10, kernel_initializer='normal', activation='relu'))
    # model.add(Dropout(0.25))
    # model.add(Dense(64, kernel_initializer='normal', activation='relu'))
    model.add(Dense(1, kernel_initializer='normal'))
    model.compile(loss='mean_absolute_error', optimizer='rmsprop')

    model.fit(X, y, nb_epoch=50, batch_size=128)

    model.save('my_model_' + str(i) + '.h5')

print('training done')

ModelList = []
t1 = time.time()
for i in range(1, 67):
    ModelList.append(load_model('my_model_' + str(i) + '.h5'))
print('models loaded')
t2 = time.time()


for model in ModelList:
    model.predict(plays[off_features].iloc[[0]])
t3 = time.time()

print('load time:' + str(t2 - t1))
print('eval time:' + str(t3 - t2))
