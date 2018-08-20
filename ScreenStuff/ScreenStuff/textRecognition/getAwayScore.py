from PIL import Image
import pytesseract
import cv2
import numpy as np
import random


def readAwayScore(frame, row1, row2, col1, col2, config, showMe, append):
    # Slice the image according to the area of the image given
    awayScoreFrame = frame[row1:row2, col1:col2]

    # Resize the sliced image into a large box
    awayScoreFrame = cv2.resize(awayScoreFrame, (100, 100))

    awayScoreApp = np.concatenate((append, awayScoreFrame), axis = 1)
    awayScoreApp = cv2.bitwise_not(awayScoreApp)

    # Shows the image if desired
    if showMe:
        cv2.imshow('Away Score Slice', awayScoreApp)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    # Converts the image to a tesseract-compatible version
    tessFrame = Image.fromarray(awayScoreApp)

    # Reads the awayScore from the sliced image if possible
    try:
        awayScore = pytesseract.image_to_string(tessFrame, config=config)[4:]
    except:
        awayScore = -1

    # Convert awayScore to an integer if possible
    try:
        awayScore = int(awayScore)
    except:
        awayScore = -1

    return awayScore


def getAwayScore(frame, computer):
    """Uses tesseract to classify the away score in the given frame"""

    # Convert the frame to gray                                                 TODO is this needed
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    # Append image
    app = cv2.imread("ScreenStuff/images/comp4Images/append.png", 0)

    # Configuration for tesseract to read only 1-4
    awayScoreConfig = "--psm 10000 -c tessedit_char_whitelist=0123456789"

    if computer == "152.1.138.157":
        as1 = readAwayScore(frame, 29, 55, 500, 540, awayScoreConfig, False, app)
        as2 = readAwayScore(frame, 30, 55, 505, 535, awayScoreConfig, False, app)
        # print(":", hs2)
        check1 = as1 == as2 and as1 != -1

        if check1:
            return as1
    elif computer == "152.1.138.158":
        as1 = readAwayScore(frame, 29, 55, 500, 540, awayScoreConfig, False, app)
        as2 = readAwayScore(frame, 30, 55, 505, 535, awayScoreConfig, False, app)
        # print(":", hs2)
        check1 = as1 == as2 and as1 != -1

        if check1:
            return as1
    elif computer == "152.1.138.160":
        as1 = readAwayScore(frame, 29, 55, 500, 540, awayScoreConfig, False, app)
        as2 = readAwayScore(frame, 30, 55, 505, 535, awayScoreConfig, False, app)
        # print(":", hs2)
        check1 = as1 == as2 and as1 != -1

        if check1:
            return as1
    elif computer == "152.1.138.159":
        as1 = readAwayScore(frame, 29, 55, 500, 540, awayScoreConfig, False, app)
        as2 = readAwayScore(frame, 30, 55, 505, 535, awayScoreConfig, False, app)
        # print(":", hs2)
        check1 = as1 == as2 and as1 != -1

        if check1:
            return as1
    else:
        as1 = readAwayScore(frame, 29, 55, 500, 540, awayScoreConfig, False, app)
        as2 = readAwayScore(frame, 30, 55, 505, 535, awayScoreConfig, False, app)
        # print(":", hs2)
        check1 = as1 == as2 and as1 != -1

        if check1:
            return as1

    path = "ScreenStuff/images/failedImages/" + computer[-3:] + "_awayscore_" + str(random.randint(1, 5)) + ".png"
    cv2.imwrite(path, frame)
    return -1

# frame = cv2.imread("ScreenStuff/images/comp4Images/6.png")
# frame = cv2.resize(frame, (1200, 800))
# print(getAwayScore(frame, "152.1.138.159"))
