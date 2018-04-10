import tensorflow as tf
import numpy as np
import pandas as pd
import time

mData = pd.read_csv("data/cleanData.csv")
plays = mData[np.isfinite(mData['Change_EP'])]
offPlays = plays[plays['Play_Num'] < 67]
offPlays = offPlays.reset_index(drop=True)
off_features = ['scoreDif', 'half', 'secs', 'firstDown', 'secondDown', 'thirdDown', 'distance', 'YTEZ', 'raiders', 'broncos']

n_nodes_hl1 = 500
n_nodes_hl2 = 500

numPlays = 66
n_classes = 1
batch_size = 20000
numFeatures = len(off_features)
inputLen = numFeatures + numPlays

X_mat = np.zeros((offPlays.shape[0], inputLen))
y_vec = np.zeros(offPlays.shape[0])
for i in range(len(X_mat)):
    playIndex = offPlays['Play_Num'].values[i] - 1
    startIndex = playIndex + numFeatures
    X_mat[i,0:numFeatures] = offPlays[off_features].values[i]
    X_mat[i,int(startIndex)] = 1
    y_vec[i] = offPlays['Change_EP'].values[i]

print("Done Reading Data")

x = tf.placeholder('float')
y = tf.placeholder('float')

hidden_1_layer = {'f_fum':n_nodes_hl1,
                  'weight':tf.Variable(tf.random_normal([inputLen, n_nodes_hl1])),
                  'bias':tf.Variable(tf.random_normal([n_nodes_hl1]))}

hidden_2_layer = {'f_fum':n_nodes_hl2,
                  'weight':tf.Variable(tf.random_normal([n_nodes_hl1, n_nodes_hl2])),
                  'bias':tf.Variable(tf.random_normal([n_nodes_hl2]))}

output_layer = {'f_fum':None,
                'weight':tf.Variable(tf.random_normal([n_nodes_hl2, n_classes])),
                'bias':tf.Variable(tf.random_normal([n_classes])),}

def neural_network_model(data):
    l1 = tf.add(tf.matmul(data,hidden_1_layer['weight']), hidden_1_layer['bias'])
    l1 = tf.nn.relu(l1)
    l2 = tf.add(tf.matmul(l1,hidden_2_layer['weight']), hidden_2_layer['bias'])
    l2 = tf.nn.relu(l2)
    output = tf.matmul(l2,output_layer['weight']) + output_layer['bias']
    return output

saver = tf.train.Saver()
tf_log = 'tf.log'

def train_neural_network(x):
    prediction = neural_network_model(x)
    cost = tf.reduce_mean(tf.square(prediction - y))
    optimizer = tf.train.AdamOptimizer().minimize(cost)

    hm_epochs = 500
    with tf.Session() as sess:

        sess.run(tf.global_variables_initializer())

        for epoch in range(hm_epochs):
            epoch_loss = 0
            for batch in range(int(len(X_mat) / batch_size)):
                start = 0 + (batch) * batch_size
                end = batch_size + (batch) * batch_size
                epoch_x = X_mat[start:end,:]
                epoch_y = y_vec[start:end]
                _, c = sess.run([optimizer, cost], feed_dict={x: epoch_x, y: epoch_y})
                epoch_loss += c
            if epoch % 20 == 0:
                print('Epoch', epoch, 'completed out of', hm_epochs,'loss:', epoch_loss)
        saver.save(sess, 'ControllerSetup/NN/my_test_model')

train_neural_network(x)

print('training done')

t1 = time.time()
with tf.Session() as sess:
    # saver = tf.train.import_meta_graph('my_test_model.meta')
    saver.restore(sess,'ControllerSetup/NN/my_test_model')
    prediction = neural_network_model(x)

    test_x = np.zeros(inputLen)
    test_x[0:numFeatures] = offPlays[off_features].values[1]
    test_x[int(offPlays['Play_Num'].values[1] - 1 + numFeatures)] = 1
    test = sess.run(prediction, feed_dict={x: test_x.reshape(1, inputLen)})
    print(test)
    print(y_vec[1])

t2 = time.time()

print('load and eval time:' + str(t2 - t1))
