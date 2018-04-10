import numpy as np
from sklearn import preprocessing
import tensorflow as tf
import pandas as pd
import time


class NNCaller:
  def __init__(self, savefile, mType="offense"):
    self.savefile = savefile
    self.type = mType

  def neural_network_model(self):
    l1 = tf.add(tf.matmul(self.inputs,self.hidden_1_layer['weight']), self.hidden_1_layer['bias'])
    l1 = tf.nn.relu(l1)
    l2 = tf.add(tf.matmul(l1,self.hidden_2_layer['weight']), self.hidden_2_layer['bias'])
    l2 = tf.nn.relu(l2)
    output = tf.matmul(l2,self.output_layer['weight']) + self.output_layer['bias']
    return output

  def build(self, numPlays, inputLen):
    n_nodes_hl1 = 1320
    n_nodes_hl2 = 1320

    self.inputs = tf.placeholder('float', name='inputs')
    self.targets = tf.placeholder('float', name='targets')
    self.hidden_1_layer = {'f_fum':n_nodes_hl1,
                           'weight':tf.Variable(tf.random_normal([inputLen, n_nodes_hl1])),
                           'bias':tf.Variable(tf.random_normal([n_nodes_hl1]))}

    self.hidden_2_layer = {'f_fum':n_nodes_hl2,
                           'weight':tf.Variable(tf.random_normal([n_nodes_hl1, n_nodes_hl2])),
                           'bias':tf.Variable(tf.random_normal([n_nodes_hl2]))}

    self.output_layer = {'f_fum':None,
                         'weight':tf.Variable(tf.random_normal([n_nodes_hl2, numPlays])),
                         'bias':tf.Variable(tf.random_normal([numPlays])),}

    self.saver = tf.train.Saver()

    self.prediction = self.neural_network_model()
    cost = tf.reduce_mean(tf.square(self.prediction - self.targets))
    return cost


  def fit(self, X, Y, batch_size, numPlays, inputLen, numEpochs):

    cost = self.build(numPlays, inputLen)
    optimizer = tf.train.AdamOptimizer().minimize(cost)

    with tf.Session() as sess:

        sess.run(tf.global_variables_initializer())

        for epoch in range(numEpochs):
            epoch_loss = 0
            for batch in range(int(len(X) / batch_size)):
                start = 0 + (batch) * batch_size
                end = batch_size + (batch) * batch_size
                epoch_x = X[start:end,:]
                epoch_y = Y[start:end,:]
                _, c = sess.run([optimizer, cost], feed_dict={self.inputs: epoch_x, self.targets: epoch_y})
                epoch_loss += c
            if epoch % 20 == 0:
                print('Epoch', epoch, 'completed out of', numEpochs,'loss:', epoch_loss)
        self.saver.save(sess, self.savefile)


  def predict(self, X):
    with tf.Session() as session:
      # restore the model
      self.saver.restore(session, self.savefile)
      P = session.run(self.prediction, feed_dict={self.inputs: X})
    return P


def main():
  mData = pd.read_csv("data/cleanData.csv")
  plays = mData[np.isfinite(mData['Change_EP'])]
  offPlays = plays[plays['Play_Num'] < 67]
  offPlays = offPlays.reset_index(drop=True)
  off_features = ['scoreDif', 'half', 'secs', 'firstDown', 'secondDown', 'thirdDown', 'distance', 'YTEZ', 'raiders', 'broncos']

  numPlays = 66
  batch_size = 10000
  numFeatures = len(off_features)
  inputLen = numFeatures * numPlays

  std_scaleENP = preprocessing.StandardScaler().fit(offPlays[['Change_EP']])
  X_mat = np.zeros((offPlays.shape[0], inputLen))
  y_mat = np.zeros((offPlays.shape[0], numPlays))
  for i in range(len(X_mat)):
      playIndex = offPlays['Play_Num'].values[i] - 1
      startIndex = playIndex * numFeatures
      endIndex = startIndex + numFeatures
      X_mat[i,int(startIndex):int(endIndex)] = offPlays[off_features].values[i]
      y_mat[i,int(playIndex)] = std_scaleENP.transform(offPlays[['Change_EP']].values[i].reshape(1,-1))

  callerModel = NNCaller("ControllerSetup/NN/testCaller")
  callerModel.fit(X_mat, y_mat, batch_size, numPlays, inputLen, 4000)
  # cost = callerModel.build(numPlays, inputLen)

  t1 = time.time()
  test = callerModel.predict(np.tile(offPlays[off_features].values[1], numPlays).reshape(1, inputLen))
  print(test)

  test2 = callerModel.predict(X_mat[0:1,:])
  print(test2)
  t2 = time.time()

  print('load and eval time:' + str(t2 - t1))

if __name__ == '__main__':
    main()
