from PIL import Image
import pytesseract
import cv2
import time

def getAskMaddenPlayName(frame):
    """
    Gets play name from madden suggested play screen.

    Args:
        frame: OpenCV BGR image
            Current frame of the game

    Returns: string
        string name of the play
    """
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    nameFrame = frame[425:480, 735:1120]

    nameFrame = cv2.bitwise_not(nameFrame)
    #nameFrame = cv2.GaussianBlur(nameFrame, (5, 5), 0)
    thresh, nameFrame = cv2.threshold(nameFrame, 100, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 11, 2)
    tessFrame = Image.fromarray(nameFrame)
    ret = pytesseract.image_to_string(tessFrame, config="--psm 10000 -c tessedit_char_whitelist=QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890")

    #cv2.imshow('frame', nameFrame)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

    if len(ret) == 0:
        nameFrame = frame[600:650, 715:900]

        nameFrame = cv2.bitwise_not(nameFrame)
        # nameFrame = cv2.GaussianBlur(nameFrame, (5, 5), 0)
        thresh, nameFrame = cv2.threshold(nameFrame, 100, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 11, 2)
        tessFrame = Image.fromarray(nameFrame)
        ret = pytesseract.image_to_string(tessFrame, config="--psm 10000 -c tessedit_char_whitelist=QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890")

        #cv2.imshow('frame', nameFrame)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()

    if len(ret) == 0:
        ret = "No play name found"

    return(ret)


#frame = cv2.imread("images/fail.png")
#frame = cv2.resize(frame, (1200, 800))
#print(len(getAskMaddenPlayName(frame)))
#print(getAskMaddenPlayName(frame))
