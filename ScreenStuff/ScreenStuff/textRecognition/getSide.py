from PIL import Image
import pytesseract
import cv2

def getSide(frame, computer):
    """
    Uses tesseract to classify the current time remaining in the quarter.

    Args:
        frame: OpenCV BGR image
            Current frame of the game

    Returns: str
        string time
    """
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    if computer == "152.1.138.157":
        frame = frame[43:46, 880:890]
        frame = cv2.bitwise_not(frame)
        frame = cv2.resize(frame, (300, 102))

        #print(sum(frame.flatten()))
#        cv2.imshow('frame', frame)
#        cv2.waitKey(0)
#        cv2.destroyAllWindows()
        if sum(frame.flatten()) > 1800000:
            ret = "own"
        else:
            ret = "opp"
    elif computer == "152.1.138.158":
        frame = frame[43:46, 880:890]
        frame = cv2.bitwise_not(frame)
        frame = cv2.resize(frame, (300, 102))

#        print(sum(frame.flatten()))
#        cv2.imshow('frame', frame)
#        cv2.waitKey(0)
#        cv2.destroyAllWindows()
        #print(sum(frame.flatten()))
        if sum(frame.flatten()) > 1200000:
            ret = "opp"
        else:
            ret = "own"
    elif computer == "152.1.138.160":
        frame = frame[43:46, 880:890]
        frame = cv2.bitwise_not(frame)
        frame = cv2.resize(frame, (300, 102))

        #print(sum(frame.flatten()))
#        cv2.imshow('frame', frame)
#        cv2.waitKey(0)
#        cv2.destroyAllWindows()
        if sum(frame.flatten()) > 1800000:
            ret = "own"
        else:
            ret = "opp"
    elif computer == "152.1.138.159":
        frame = frame[43:46, 880:890]
        frame = cv2.bitwise_not(frame)
        frame = cv2.resize(frame, (300, 102))

        #print(sum(frame.flatten()))
#        cv2.imshow('frame', frame)
#        cv2.waitKey(0)
#        cv2.destroyAllWindows()
        if sum(frame.flatten()) > 750000:
            ret = "opp"
        else:
            ret = "own"
    else:
        frame = frame[43:46, 880:890]
        frame = cv2.bitwise_not(frame)
        frame = cv2.resize(frame, (300, 102))

        #print(sum(frame.flatten()))
#        cv2.imshow('frame', frame)
#        cv2.waitKey(0)
#        cv2.destroyAllWindows()
        if sum(frame.flatten()) > 750000:
            ret = "opp"
        else:
            ret = "own"

    return(ret)

#frame = cv2.imread("ScreenStuff/images/failedImages/157_time_4.png")
#frame = cv2.resize(frame, (1200, 800))
#print(getSide(frame, "152.1.138.157"))
