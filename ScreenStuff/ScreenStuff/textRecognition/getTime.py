from PIL import Image
import pytesseract
import cv2
import random


def readTime(frame, row1, row2, col1, col2, config, showMe):
    # Slice the image according to the area of the image given
    timeFrame = frame[row1:row2, col1:col2]

    # Resize the sliced image into a large box
    timeFrame = cv2.resize(timeFrame, (100, 100))

    # Shows the image if desired
    if showMe:
        cv2.imshow('Time Slice', timeFrame)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    # Converts the image to a tesseract-compatible version
    tessFrame = Image.fromarray(timeFrame)

    # Reads the time from the sliced image if possible
    try:
        time = pytesseract.image_to_string(tessFrame, config = config)
        #print(time)
    except:
        time = -1

    try:
        if time[1] == ":" and len(time) == 4:
            time = int(time[0]) * 60 + int(time[2:])
            return time
        elif time == "8000":
            time = 480
        elif time == "0008":
            time = 8
        elif time == "0118":
            time = 8
        elif time == "0 08":
            time = 8
        elif len(time) == 3 and (time[0] == "1" or time[0] == "4"):
            time = int(time[0]) * 60 + int(time[1:])
        else:
            time = -1
    except:
        time = -1

    return time



def getTime(frame, computer):
    """
    Uses tesseract to classify the time in the given frame

    Args:
        frame: OpenCV image
            Current frame of the game
        computer: str
            ID of the computer the frame was taken from

    Returns: int
        time from 1 to 4
    """

    # Convert the frame to gray                                                 TODO is this needed
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    # Configuration for tesseract to read only 1-4
    timeConfig = "--psm 10000 -c tessedit_char_whitelist=0123456789:"

    if computer == "152.1.138.157":
        time1 = readTime(frame, 30, 57, 784, 826, timeConfig, False)
        time2 = readTime(frame, 30, 55, 786, 824, timeConfig, False)
        #print(time1, time2)

        check1 = time1 == time2 and time1 != -1

        if check1:
            return time1
        else:
            time3 = readTime(frame, 32, 54, 788, 822, timeConfig, False)

            check3 = (time1 == time3 or time2 == time3) and time3 != -1

            if check3:
                return time3
            else:
                check4 = time3 != -1
                if check4:
                    return time3
                else:
                    pass
    elif computer == "152.1.138.158":
        time1 = readTime(frame, 30, 57, 784, 826, timeConfig, False)
        time2 = readTime(frame, 30, 55, 786, 824, timeConfig, False)
        #print(time1, time2)

        check1 = time1 == time2 and time1 != -1

        if check1:
            return time1
        else:
            time3 = readTime(frame, 32, 54, 788, 822, timeConfig, False)

            check3 = (time1 == time3 or time2 == time3) and time3 != -1

            if check3:
                return time3
            else:
                check4 = time3 != -1
                if check4:
                    return time3
                else:
                    pass
    elif computer == "152.1.138.160":
        time1 = readTime(frame, 30, 57, 784, 826, timeConfig, False)
        time2 = readTime(frame, 30, 55, 786, 824, timeConfig, False)
        #print(time1, time2)

        check1 = time1 == time2 and time1 != -1

        if check1:
            return time1
        else:
            time3 = readTime(frame, 32, 54, 788, 822, timeConfig, False)

            check3 = (time1 == time3 or time2 == time3) and time3 != -1

            if check3:
                return time3
            else:
                check4 = time3 != -1
                if check4:
                    return time3
                else:
                    pass
    elif computer == "152.1.138.159":
        time1 = readTime(frame, 30, 57, 784, 826, timeConfig, False)
        time2 = readTime(frame, 30, 55, 786, 824, timeConfig, False)
        #print(time1, time2)

        check1 = time1 == time2 and time1 != -1

        if check1:
            return time1
        else:
            time3 = readTime(frame, 32, 54, 788, 822, timeConfig, False)
            #print(time3)

            check3 = (time1 == time3 or time2 == time3) and time3 != -1

            if check3:
                return time3
            else:
                check4 = time3 != -1
                if check4:
                    return time3
                else:
                    check5 = time1 == 480 or time2 == 480 or time3 == 480
                    if check5:
                        return 480

    else:
        time1 = readTime(frame, 30, 57, 784, 826, timeConfig, False)
        time2 = readTime(frame, 30, 55, 786, 824, timeConfig, False)
        #print(time1, time2)

        check1 = time1 == time2 and time1 != -1

        if check1:
            return time1
        else:
            time3 = readTime(frame, 32, 54, 788, 822, timeConfig, False)

            check3 = (time1 == time3 or time2 == time3) and time3 != -1

            if check3:
                return time3
            else:
                check4 = time3 != -1
                if check4:
                    return time3
                else:
                    pass


    path = "ScreenStuff/images/failedImages/" + computer[-3:] + "_time_" + str(random.randint(1, 5)) + ".png"
    cv2.imwrite(path, frame)
    return -1

# frame = cv2.imread("ScreenStuff/images/failedImages/159_time_3.png")
# frame = cv2.resize(frame, (1200, 800))
# print(getTime(frame, "152.1.138.159"))
