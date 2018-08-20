from PIL import Image
import pytesseract
import cv2
import numpy as np
import random


def readFieldPos(frame, row1, row2, col1, col2, config, showMe, append):
    # Slice the image according to the area of the image given
    fieldPosFrame = frame[row1:row2, col1:col2]

    # Resize the sliced image into a large box
    fieldPosFrame = cv2.resize(fieldPosFrame, (100, 100))

    fieldPosApp = np.concatenate((append, fieldPosFrame), axis = 1)
    fieldPosApp = cv2.bitwise_not(fieldPosApp)

    # Shows the image if desired
    if showMe:
        cv2.imshow('Home Score Slice', fieldPosApp)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    # Converts the image to a tesseract-compatible version
    tessFrame = Image.fromarray(fieldPosApp)

    # Reads the fieldPos from the sliced image if possible
    try:
        fieldPos = pytesseract.image_to_string(tessFrame, config=config)[4:]
        #print(fieldPos)
    except:
        fieldPos = -1

    # Convert fieldPos to an integer if possible
    try:
        fieldPos = int(fieldPos)
    except:
        fieldPos = -1

    return fieldPos


def getFieldPos(frame, computer):
    """Uses tesseract to classify the home score in the given frame"""

    # Convert the frame to gray                                                 TODO is this needed
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    # Append image
    app = cv2.imread('ScreenStuff/images/comp4Images/append.png', 0)

    # Configuration for tesseract to read only 1-4
    fieldPosConfig = "--psm 10000 -c tessedit_char_whitelist=0123456789"

    if computer == "152.1.138.157":
        fieldPos1 = readFieldPos(frame, 28, 60, 845, 875, fieldPosConfig, False, app)
        fieldPos2 = readFieldPos(frame, 28, 60, 850, 875, fieldPosConfig, False, app)
        #print(fieldPos1, fieldPos2)
        # print(":", hs2)
        check1 = fieldPos1 == fieldPos2 and fieldPos1 != -1 and fieldPos1 < 100

        if check1:
            return fieldPos1
        else:
            fieldPos3 = readFieldPos(frame, 28, 55, 850, 873, fieldPosConfig, False, app)
            #print(fieldPos3)
            check2 = (fieldPos3 == fieldPos1 or fieldPos3 == fieldPos2) and fieldPos3 != -1
            if check2:
                return fieldPos3

    elif computer == "152.1.138.158":
        fieldPos1 = readFieldPos(frame, 28, 60, 845, 875, fieldPosConfig, False, app)
        fieldPos2 = readFieldPos(frame, 28, 60, 850, 875, fieldPosConfig, False, app)
        # print(":", hs2)
        check1 = fieldPos1 == fieldPos2 and fieldPos1 != -1 and fieldPos1 < 100

        if check1:
            return fieldPos1
    elif computer == "152.1.138.160":
        fieldPos1 = readFieldPos(frame, 28, 60, 845, 875, fieldPosConfig, False, app)
        fieldPos2 = readFieldPos(frame, 28, 60, 850, 875, fieldPosConfig, False, app)
        # print(":", hs2)
        check1 = fieldPos1 == fieldPos2 and fieldPos1 != -1 and fieldPos1 < 100

        if check1:
            return fieldPos1
        else:
            fieldPos3 = readFieldPos(frame, 28, 55, 850, 873, fieldPosConfig, False, app)
            #print(fieldPos3)
            check2 = (fieldPos3 == fieldPos1 or fieldPos3 == fieldPos2) and fieldPos3 != -1
            if check2:
                return fieldPos3
    elif computer == "152.1.138.159":
        fieldPos1 = readFieldPos(frame, 28, 60, 845, 875, fieldPosConfig, False, app)
        fieldPos2 = readFieldPos(frame, 28, 60, 850, 875, fieldPosConfig, False, app)
        # print(":", hs2)
        check1 = fieldPos1 == fieldPos2 and fieldPos1 != -1 and fieldPos1 < 100

        if check1:
            return fieldPos1
    else:
        fieldPos1 = readFieldPos(frame, 28, 60, 845, 875, fieldPosConfig, False, app)
        fieldPos2 = readFieldPos(frame, 28, 60, 850, 875, fieldPosConfig, False, app)
        # print(":", hs2)
        check1 = fieldPos1 == fieldPos2 and fieldPos1 != -1 and fieldPos1 < 100

        if check1:
            return fieldPos1


    path = "ScreenStuff/images/failedImages/" + computer[-3:] + "_fieldpos_" + str(random.randint(1, 5)) + ".png"
    cv2.imwrite(path, frame)
    return -1

# frame = cv2.imread("ScreenStuff/images/failedImages/160_fieldpos_5.png")
# frame = cv2.resize(frame, (1200, 800))
# print(getFieldPos(frame, "152.1.138.160"))
