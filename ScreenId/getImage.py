import numpy as np
import datetime
import cv2
import mss
import sys
import time

with mss.mss() as sct:
    time.sleep(30.0)
    monitor = {'top': -2160, 'left': 0, 'width': 3840, 'height': 2160}
    # monitor = {'top': 0, 'left': 0, 'width': 1280, 'height': 720}
    # frame = np.array(sct.grab(monitor))
    # frame = cv2.resize(frame, (1200, 800))
    #
    # frame = frame[25:65, 250:300]
    #
    # cv2.imshow('frame', frame)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    form = "callplay"
    # form = "kickoff"
    for i in range(61, 90):
        frame = np.array(sct.grab(monitor))
        frame = cv2.resize(frame, (1200, 800))

        # frame = frame[25:65, 250:300]
        cv2.imwrite("images/" + form + "_0" + str(i) + ".png", frame)
        time.sleep(2.0)

    # for i in range(10, 500):
    #     frame = np.array(sct.grab(monitor))
    #     frame = cv2.resize(frame, (1200, 800))
    #
    #     # frame = frame[25:65, 250:300]
    #     cv2.imwrite("images/" + form + "_" + str(i) + ".png", frame)
    #     time.sleep(4.0)
