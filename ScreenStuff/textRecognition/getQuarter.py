from datetime import datetime as dt
from PIL import Image
import pytesseract
import sys
import cv2

def qtrSlice(frame, rowSlice1, rowSlice2, colSlice1, colSlice2, config, showMe):
    qtrFrame = frame[rowSlice1:rowSlice2, colSlice1:colSlice2]
    qtrFrame = cv2.resize(qtrFrame, (100, 102))
    tessFrame = Image.fromarray(qtrFrame)
    if showMe:
        cv2.imshow('Frame', qtrFrame)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    try:
        qtr = pytesseract.image_to_string(tessFrame, config=config)[0]
    except:
        qtr = ""
    return qtr

def getQuarter(frame, debug):
    """
    Uses tesseract to classify the current quarter.

    Args:
        frame: OpenCV BGR image
            Current frame of the game

    Returns: str
        string quarter
    """
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    qtrConfig = "--psm 10000 -c tessedit_char_whitelist=1234O"

    qtr1 = qtrSlice(frame, 25, 66, 715, 765, qtrConfig, False)

    check1 = qtr1 != ""

    if check1:
        if qtr1 == "O":
            qtr1 = 4
        else:
            try:
                qtr1 = int(qtr1)
            except:
                if debug == False:
                    # Establish filepath for writing failed image
                    f1 = "C:/Users/npkapur/Documents/Madden/images/"
                    f2 = "failedImages/qtr_"
                    f3 = str(dt.now()).split(" ")[0] + "_"
                    f4 = str(dt.now()).split(" ")[1].split(":")[0] + "_"
                    f5 = str(dt.now()).split(" ")[1].split(":")[1] + "_"
                    f6 = str(dt.now()).split(" ")[1].split(":")[2].split(".")[0]
                    failPath = f1 + f2 + f3 + f4 + f5 + f6 + ".png"
                    cv2.imwrite(failPath, frame)
                    return -1

            return qtr1

    if debug == False:
        # Establish filepath for writing failed image
        f1 = "C:/Users/npkapur/Documents/Madden/images/"
        f2 = "failedImages/qtr_"
        f3 = str(dt.now()).split(" ")[0] + "_"
        f4 = str(dt.now()).split(" ")[1].split(":")[0] + "_"
        f5 = str(dt.now()).split(" ")[1].split(":")[1] + "_"
        f6 = str(dt.now()).split(" ")[1].split(":")[2].split(".")[0]
        failPath = f1 + f2 + f3 + f4 + f5 + f6 + ".png"
        cv2.imwrite(failPath, frame)
    else:
        pass
        # print(qtr1)

    return -1


#frame = cv2.imread("images/failedImages/qtr_2017-10-27_12_55_35.png")
#frame = cv2.resize(frame, (1200, 800))
#print(getQuarter(frame, True))
