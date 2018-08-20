from PIL import Image
import pytesseract
import datetime
import cv2
import random

def getFinalScore(frame, oldHome, oldAway, computer):
    """
    Uses tesseract to read the final score of the game.

    Args:
        frame: OpenCV BGR image
            Frame containing the end screen of the game

    Returns: tuple
        tuple that contains the final score for the home and away teams
    """
    config = "--psm 10000 -c tessedit_char_whitelist=0123456789"

    awayScore = frame[325:365, 90:125]
    awayScore = cv2.resize(awayScore, (100, 100))

    tessFrame = Image.fromarray(awayScore)

    flag = 0

    try:
        awayScore = pytesseract.image_to_string(tessFrame, config = config)
    except:
        awayScore = oldAway
        flag = 1

    homeScore = frame[330:360, 1070:1100]
    homeScore = cv2.resize(homeScore, (100, 100))

    tessFrame = Image.fromarray(homeScore)

    try:
        homeScore = pytesseract.image_to_string(tessFrame, config = config)
    except:
        homeScore = oldHome
        flage = 1

    try:
        homeScore = int(homeScore)
    except:
        homeScore = oldHome
        flag = 1

    try:
        awayScore = int(awayScore)
    except:
        awayScore = oldAway
        flag = 1

    if flag == 1:
        path = "ScreenStuff/images/failedImages/" + computer[-3:] + "_finalscore_" + str(random.randint(1, 5)) + ".png"
        cv2.imwrite(path, frame)


    return awayScore, homeScore

#img = cv2.imread("ScreenStuff/images/formationImages/44.png")
#print(getFinalScore(img))
