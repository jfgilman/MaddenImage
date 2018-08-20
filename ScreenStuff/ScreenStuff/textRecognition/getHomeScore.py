from PIL import Image
import pytesseract
import cv2
import numpy as np
import random


def readHomeScore(frame, row1, row2, col1, col2, config, showMe, append):
    # Slice the image according to the area of the image given
    homeScoreFrame = frame[row1:row2, col1:col2]

    # Resize the sliced image into a large box
    homeScoreFrame = cv2.resize(homeScoreFrame, (100, 100))

    homeScoreApp = np.concatenate((append, homeScoreFrame), axis = 1)
    homeScoreApp = cv2.bitwise_not(homeScoreApp)

    # Shows the image if desired
    if showMe:
        cv2.imshow('Home Score Slice', homeScoreApp)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    # Converts the image to a tesseract-compatible version
    tessFrame = Image.fromarray(homeScoreApp)

    # Reads the homeScore from the sliced image if possible
    try:
        homeScore = pytesseract.image_to_string(tessFrame, config=config)[4:]
        #print(homeScore)
    except:
        homeScore = -1

    # Convert homeScore to an integer if possible
    try:
        homeScore = int(homeScore)
    except:
        homeScore = -1

    return homeScore


def getHomeScore(frame, computer):
    """Uses tesseract to classify the home score in the given frame"""

    # Convert the frame to gray                                                 TODO is this needed
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    # Append image
    app = cv2.imread('ScreenStuff/images/comp4Images/append.png', 0)

    # Configuration for tesseract to read only 1-4
    homeScoreConfig = "--psm 10000 -c tessedit_char_whitelist=0123456789"

    if computer == "152.1.138.157":
        hs1 = readHomeScore(frame, 28, 60, 670, 699, homeScoreConfig, False, app)
        hs2 = readHomeScore(frame, 28, 60, 665, 700, homeScoreConfig, False, app)

        check1 = hs1 == hs2 and hs1 != -1

        if check1:
            return hs1
    elif computer == "152.1.138.158":
        hs1 = readHomeScore(frame, 28, 60, 670, 699, homeScoreConfig, False, app)
        hs2 = readHomeScore(frame, 28, 60, 665, 700, homeScoreConfig, False, app)

        check1 = hs1 == hs2 and hs1 != -1

        if check1:
            return hs1
    elif computer == "152.1.138.160":
        hs1 = readHomeScore(frame, 28, 60, 670, 699, homeScoreConfig, False, app)
        hs2 = readHomeScore(frame, 28, 60, 665, 700, homeScoreConfig, False, app)

        check1 = hs1 == hs2 and hs1 != -1

        if check1:
            return hs1
    elif computer == "152.1.138.159":
        hs1 = readHomeScore(frame, 28, 60, 670, 699, homeScoreConfig, False, app)
        hs2 = readHomeScore(frame, 28, 60, 665, 700, homeScoreConfig, False, app)
        # print(":", hs2)
        check1 = hs1 == hs2 and hs1 != -1

        if check1:
            return hs1
    else:
        hs1 = readHomeScore(frame, 28, 60, 670, 699, homeScoreConfig, False, app)
        hs2 = readHomeScore(frame, 28, 60, 665, 700, homeScoreConfig, False, app)

        check1 = hs1 == hs2 and hs1 != -1

        if check1:
            return hs1


    path = "ScreenStuff/images/failedImages/" + computer[-3:] + "_homescore_" + str(random.randint(1, 5)) + ".png"
    cv2.imwrite(path, frame)
    return -1

#frame = cv2.imread("ScreenStuff/images/comp3Images/0.png")
#frame = cv2.resize(frame, (1200, 800))
#print(getHomeScore(frame, "152.1.138.160"))
