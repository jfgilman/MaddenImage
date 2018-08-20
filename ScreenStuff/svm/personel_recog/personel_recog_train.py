from skimage.feature import hog
from imutils import paths
from sklearn import svm
import argparse
import cv2
import numpy as np
import pickle

# run this line in the game_state_recog directory to trian
# python personel_recog_train.py --training images/training --testing images/testing

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-t", "--training", required=True, help="path to the training images")
ap.add_argument("-e", "--testing", required=True, help="path to the tesitng images")
args = vars(ap.parse_args())

data = []
labels = []

# loop over the training images
for imagePath in paths.list_images(args["training"]):
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    fd = hog(gray, orientations=8, pixels_per_cell=(16, 16), cells_per_block=(1, 1))

	# extract the label from the image path, then update the
	# label and data lists
    labels.append(imagePath.split("\\")[-2])
    data.append(fd)

# # train a Linear SVM on the data
# model = LinearSVC(C=100.0, random_state=42)
model = svm.SVC(gamma=0.0002, C=10)
model.fit(data, labels)

# loop over the testing images
for imagePath in paths.list_images(args["testing"]):
	# load the image, convert it to grayscale, describe it,
	# and classify it
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    fd = hog(gray, orientations=8, pixels_per_cell=(16, 16), cells_per_block=(1, 1))

    prediction = model.predict(fd)[0]

	# display the image and the prediction
    cv2.putText(image, prediction, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 3)
    cv2.imshow("Image", image)
    cv2.waitKey(0)


# save the model to disk
filename = 'finalized_offPersonel_model.sav'
pickle.dump(model, open(filename, 'wb'))

# # load the model from disk
# loaded_model = pickle.load(open(filename, 'rb'))


# getFrame code
