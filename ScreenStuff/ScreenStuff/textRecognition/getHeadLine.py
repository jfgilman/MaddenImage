from PIL import Image
import pytesseract
import cv2


def getHeadLine(frame):
    """
    Gets headline from play call screen screen.

    Args:
        frame: OpenCV BGR image
            Current frame of the game

    Returns: string
        screen title
    """
    #frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    frame1 = frame[115:155, 800:1100]

    frame1 = cv2.bitwise_not(frame1)
    # frame = cv2.GaussianBlur(frame1, (5, 5), 0)
    thresh, frame1 = cv2.threshold(frame1, 100, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 11, 2)
    tessFrame = Image.fromarray(frame1)
    ret = pytesseract.image_to_string(tessFrame, config="-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    #print(ret)

    # cv2.imshow('frame', frame1)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    if "FILTER" in ret:
        return("FILTER")
    elif "SUGGEST" in ret:
        return("SUGGESTIONS")
    elif "FORMATION" in ret:
        #print("Formation screen")
        return("FORMATION")
    else:
        return("OTHER")

#frame = cv2.imread("images/runImages/form2.png")
#frame = cv2.resize(frame, (1200, 800))
#print(getHeadLine(frame))

# frame = cv2.imread("31.png")
# frame = cv2.resize(frame, (1200, 800))
# print(len(getAskMaddenPlayName(frame)))
# print(getAskMaddenPlayName(frame))
