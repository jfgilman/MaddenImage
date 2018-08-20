from PIL import Image
import pytesseract
import cv2

frame = cv2.imread('ScreenStuff/images/comp4Images/1.png')
frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
frame = cv2.resize(frame, (1200, 800))

TOAwayImg = frame[27:61, 492:501]
print(sum(TOAwayImg.flatten()))
cv2.imshow('img', TOAwayImg)
cv2.waitKey(0)
cv2.destroyAllWindows()




def getDistance(frame, computer):
    """
    Uses tesseract to classify the distance in the given frame

    Args:
        frame: OpenCV image
            Current frame of the game
        computer: str
            ID of the computer the frame was taken from

    Returns: str
        Distance from 1 to 99 (this is just an example, obv goal, distance
        must be accounted for)
    """

    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)                             #TODO is this needed
    # distConfig = "--psm 10000 -c tessedit_char_whitelist=0123456789&"

    if computer == "152.1.138.157":
        pass
    elif computer == "152.1.138.158":
        pass
    elif computer == "152.1.138.160":
        pass
    elif computer == "152.1.138.159":
        pass
        # Slice in two most commonly correct ways
        # Check that they equal one another
        # Convert and return
        # If necessary go deeper
        # Hit this with a decorator at first and log file
    else:
        pass
