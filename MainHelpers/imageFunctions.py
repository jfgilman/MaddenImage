import cv2
import numpy as np
import mss
import time
from skimage.feature import hog
from ScreenStuff.textRecognition.getHeadLine import getHeadLine
from ScreenStuff.textRecognition.getTime import getTime
from ScreenStuff.textRecognition.getAskMaddenPlayName import getAskMaddenPlayName
import random




filters = {"AskMadden": 1, "Formation": 2, "Concept": 4, "PlayType": 5,
           "RunPass": 3, "Recent": 6, "Super": 7}

def defenseUpdates(screenType, gray, loaded_offPersonel_model, game):
    if screenType == "defense":
        #game.updateHomeBall(False)
        game.offPersonel = getScreenType(gray[660:690, 175:280], loaded_offPersonel_model)
    else:
        #game.updateHomeBall(True)
        game.offPersonel = None


def checkStuck(stuckCount, pi):
    """
    Checks if the game has been stuck (likely waiting to snap) for too long.
    If it has, press buttons to try to remedy this.

    args:
        stuckCount: int
            The number of consecutive frames for which the game has been on the
            "other" screen
        pi: RasPi object
            Raspberry pi to execute button presses

    returns:
        stuckCount: int
            Either 0 or the same number that was passed to the function
    """
    if stuckCount > 2000:
        # Execute button presses for high count
        pi.send("Press A")
        time.sleep(1)
        pi.send("Press A")
        time.sleep(2)
        pi.send("Press A")
        time.sleep(2)

        # Reset the count to 0
        return 0
    else:
        return stuckCount


def prepFrame(sct, monitor):
    frame = np.array(sct.grab(monitor))
    frame = cv2.resize(frame, (1200, 800))
    return frame


def grayFrame(frame):
    try:
        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        return gray
    except:
        return "Bad Frame"


def getScreenType(gray, loaded_model):
    fd = hog(gray, orientations=8, pixels_per_cell=(16, 16),
              cells_per_block=(1, 1))
    screenType = loaded_model.predict(fd.reshape(1,-1))[0]
    return screenType


def prepClockFrames(sct, monitor, frame):
    time.sleep(1)
    trueFrame = prepFrame(sct, monitor)
    return frame, trueFrame


def confirmScreenType(frame, loaded_model):
    gray = grayFrame(frame)
    fd = hog(gray, orientations=8, pixels_per_cell=(16, 16),
             cells_per_block=(1, 1))
    screenType = loaded_model.predict(fd.reshape(1, -1))[0]
    return screenType


def checkClockRunning(frame1, frame2, game):
    firstTime = getTime(frame1, game.CPUID)
    secondTime = getTime(frame2, game.CPUID)
    differentTimes = firstTime != secondTime
    validTimes = firstTime != -1 and secondTime != -1
    if differentTimes and validTimes:
        return True
    else:
        return False


def randomInitialize(sct, monitor, pi):
    #pi.send("Press B")
    #time.sleep(2)                                                               #TODO test this timing
    headlineFrame = prepFrame(sct, monitor)
    grayHeadline = grayFrame(headlineFrame)
    #cv2.imshow('frame', headlineFrame)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    #grayHeadline = cv2.resize(grayHeadline[120:160, 675:1130], (1200, 800))
    #headline = getScreenType(grayHeadline, loaded_headline_model)
    headline = getHeadLine(grayHeadline)
    return headline


def otherReset(sct, monitor, pi):
    for i in range(2):
        pi.send("Press B")
        time.sleep(2)

    headline = randomInitialize(sct, monitor, pi)
    return headline


def execSpecialTeams(sct, monitor, game, pi):
    pi.send("Press A")
    time.sleep(7)
    hashFrame = prepFrame(sct, monitor)
    #time.sleep(2)
    #try:
    #    print(1, direction)
    #except:
    #    pass
    direction = hashCheck(hashFrame)
    #print(2, direction)
    #path = "ScreenStuff/images/hashImages/" + str(random.randint(1, 50)) + ".png"
    pi.kick(direction, game.difficulty)


def execAskMadden(sct, monitor, screenType, game, pi):
    frame = prepFrame(sct, monitor)
    maddenPlay = getAskMaddenPlayName(frame)
    #print(maddenPlay)
    kick, kickType = checkSpecialTeams(maddenPlay)
    if kick:
        execSpecialTeams(sct, monitor, game, pi)
    else:
        pi.callMadden(screenType)
    return kickType


def formationSnap(formNum, setNum, possession, sct, monitor):
    frame = prepFrame(sct, monitor)
    if possession == True:
        path = "images/formationImages/home_" + str(formNum) + "_" + str(setNum) + "_" + str(datetime.datetime.now())[11:13] + "_" + str(datetime.datetime.now())[14:16] + "_"
        path2 = str(datetime.datetime.now())[17:19] + ".png"
        path = path + path2
        cv2.imwrite(path, frame)
    else:
        path = "images/formationImages/away_" + str(formNum) + "_" + str(setNum) + "_" + str(datetime.datetime.now())[11:13] + "_" + str(datetime.datetime.now())[14:16] + "_"
        path2 = str(datetime.datetime.now())[17:19] + ".png"
        path = path + path2
        cv2.imwrite(path, frame)

def callTimeout(H1TOLeft, H2TOLeft, clockRunning, awayScore, homeScore, down,
                timeOnClock, offense, quarter, yardsToTD):
    scoreDif = homeScore - awayScore
    if clockRunning:
        if quarter == 2 and offense and timeOnClock < 120 and yardsToTD <= 65 and H1TOLeft > 0:
            if down == 4:
                pass
            else:
                return True
        elif quarter == 4 and timeOnClock < 180 and scoreDif < 0 and H2TOLeft > 0 and timeOnClock > 0:
            return True
    elif quarter == 4 and scoreDif == 0 and timeOnClock < 120 and offense and down < 4 and H2TOLeft > 0:
        return True
    else:
        return False

def navigateToFormation(filterCursor, pi):
    filterNumber = filters[filterCursor]
    if filterNumber >= 2:
        buttonPresses = filterNumber - 2
        for i in range(buttonPresses):
            pi.send("Press UP")
            time.sleep(0.5)
        pi.send("Press A")
        time.sleep(1.5)
    else:
        pi.send("Press DOWN")
        time.sleep(0.5)
        pi.send("Press A")
        time.sleep(1.5)

def navigateToAskMadden(filterCursor, pi):
    filterNumber = filters[filterCursor]
    buttonPresses = filterNumber - 1
    for i in range(buttonPresses):
        pi.send("Press UP")
        time.sleep(0.5)
    pi.send("Press A")
    time.sleep(1)

def checkSpecialTeams(playCall):
    upperCase = playCall.upper()
    if "PUNT" in upperCase:
        return True, "PUNT"
    elif "FIELD" in upperCase:
        return True, "FG"
    elif "PAT" in upperCase:
        return True, None
    else:
        return False, None

def hashCheck(frame):
    #frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    # if game.down == "5":
    #     return "center"

    frame1 = frame[400:430, 0:10]

    #frame1 = cv2.bitwise_not(frame1)
    frame1Vec = frame1.flatten()
    frame1VecSum = sum(frame1Vec)
    print(frame1VecSum)
    #cv2.imshow('frame', frame1)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    #print(frame1VecSum)
    if frame1VecSum > 160000:
        ret = "left"
    # if ret == "left":
    #     frame2 = frame[400:432, 1191:1200]
    #     frame2 = cv2.bitwise_not(frame)
    #     frame2Vec = frame2.flatten()
    #     frame2VecSum = sum(frame2Vec)
    #     cv2.imshow('frame', frame2)
    #     cv2.waitKey(0)
    #     ret = "center"
    else:
        frame2 = frame[330:355, 0:10]
        frame2Vec = frame2.flatten()
        frame2VecSum = sum(frame2Vec)
        #cv2.imshow('frame', frame2)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()
        #print(frame2VecSum)
        if frame2VecSum > 160000:
            ret = "center"
        else:
            ret = "right"
        #cv2.imshow('frame', frame2)
        #cv2.waitKey(0)
        #ret = "right"
        #frame = cv2.GaussianBlur(frame, (5, 5), 0)
    # thresh, frame = cv2.threshold(frame, 100, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 11, 2)
    # frame1 = cv2.resize(frame, (100,102))
    # frame2 = cv2.resize(frame, (200, 200)) #changed values
    # tessFrame = Image.fromarray(frame2)
    # ret = pytesseract.image_to_string(tessFrame, config="--psm 10000 -c tessedit_char_whitelist=0123456789")
    # cv2.imshow('frame', frame2)
    # cv2.waitKey(0)
    #cv2.destroyAllWindows()
    # if ret == "":
    #      #doesn't recognize 0 alone, so this is a measure to prevent that
    #     tessFrame = Image.fromarray(frame1)
    #     ret = pytesseract.image_to_string(tessFrame, config="--psm 10000 -c tessedit_char_whitelist=0123456789")
    #     cv2.imshow('frame1', frame1)
    #     cv2.waitKey(0)
    return(ret)
