from PIL import Image
import pytesseract
import cv2
import random


def readDist(frame, row1, row2, col1, col2, config, showMe):
    # Slice the image according to the area of the image given
    distFrame = frame[row1:row2, col1:col2]

    # Resize the sliced image into a large box
    distFrame = cv2.resize(distFrame, (100, 100))

    # Shows the image if desired
    if showMe:
        cv2.imshow('dist Slice', distFrame)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    # Converts the image to a tesseract-compatible version
    tessFrame = Image.fromarray(distFrame)

    # Reads the dist from the sliced image if possible
    try:
        dist = pytesseract.image_to_string(tessFrame, config = config)
        #print(dist)
    except:
        dist = -1

    if len(dist) > 4:
        dist = -1

    try:
        if dist[-2] == "&":
            dist = int(dist[-1])
        elif dist[-3] == "&":
            dist = int(dist[-2:])
        elif dist == "8110" or dist == "8410":
            dist = 10
    except:
        dist = -1

    try:
        dist = int(dist)
    except:
        dist = -1

    return dist



def getDistance(frame, computer):
    """
    Uses tesseract to classify the dist in the given frame

    Args:
        frame: OpenCV image
            Current frame of the game
        computer: str
            ID of the computer the frame was taken from

    Returns: int
        dist from 1 to 4
    """

    # Convert the frame to gray                                                 TODO is this needed
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    # Configuration for tesseract to read only 1-4
    distConfig = "--psm 10000 -c tessedit_char_whitelist=0123456789&"

    if computer == "152.1.138.157":
        dist1 = readDist(frame, 32, 55, 335, 372, distConfig, False)
        dist2 = readDist(frame, 30, 55, 334, 370, distConfig, False)
        #print(dist1, dist2)

        check1 = dist1 == dist2 and dist1 != -1 and dist1 < 100

        if check1:
            return dist1
        else:
            dist3 = readDist(frame, 32, 56, 336, 374, distConfig, False)

            check3 = (dist1 == dist3 or dist2 == dist3) and dist3 != -1 and dist3 < 100

            if check3:
                return dist3
            else:
                frame = frame[25:65, 330:380]
                frameVec = frame.flatten()
                if sum(frameVec) > 175000:
                    return 0
                elif sum(frameVec) > 168000:
                    return 0.5
                else:
                    pass
    elif computer == "152.1.138.158":
        dist1 = readDist(frame, 32, 55, 335, 372, distConfig, False)
        dist2 = readDist(frame, 30, 55, 334, 370, distConfig, False)
        #print(dist1, dist2)

        check1 = dist1 == dist2 and dist1 != -1 and dist1 < 100

        if check1:
            return dist1
        else:
            dist3 = readDist(frame, 32, 56, 336, 374, distConfig, False)

            check3 = (dist1 == dist3 or dist2 == dist3) and dist3 != -1 and dist3 < 100

            if check3:
                return dist3
            else:
                frame = frame[25:65, 330:380]
                frameVec = frame.flatten()
                if sum(frameVec) > 175000:
                    return 0
                elif sum(frameVec) > 168000:
                    return 0.5
                else:
                    pass
    elif computer == "152.1.138.160":
        dist1 = readDist(frame, 32, 55, 335, 372, distConfig, False)
        dist2 = readDist(frame, 30, 55, 334, 370, distConfig, False)
        #print(dist1, dist2)

        check1 = dist1 == dist2 and dist1 != -1 and dist1 < 100

        if check1:
            return dist1
        else:
            dist3 = readDist(frame, 32, 56, 336, 374, distConfig, False)

            check3 = (dist1 == dist3 or dist2 == dist3) and dist3 != -1 and dist3 < 100

            if check3:
                return dist3
            else:
                frame = frame[25:65, 330:380]
                frameVec = frame.flatten()
                if sum(frameVec) > 175000:
                    return 0
                elif sum(frameVec) > 168000:
                    return 0.5
                else:
                    pass
    elif computer == "152.1.138.159":
        dist1 = readDist(frame, 32, 55, 335, 372, distConfig, False)
        dist2 = readDist(frame, 30, 55, 334, 370, distConfig, False)
        #print(dist1, dist2)

        check1 = dist1 == dist2 and dist1 != -1 and dist1 < 100

        if check1:
            return dist1
        else:
            dist3 = readDist(frame, 32, 56, 336, 374, distConfig, False)

            check3 = (dist1 == dist3 or dist2 == dist3) and dist3 != -1 and dist3 < 100

            if check3:
                return dist3
            else:
                frame = frame[25:65, 330:380]
                frameVec = frame.flatten()
                if sum(frameVec) > 175000:
                    return 0
                elif sum(frameVec) > 168000:
                    return 0.5
                else:
                    pass

    else:
        dist1 = readDist(frame, 32, 55, 335, 372, distConfig, False)
        dist2 = readDist(frame, 30, 55, 334, 370, distConfig, False)
        #print(dist1, dist2)

        check1 = dist1 == dist2 and dist1 != -1 and dist1 < 100

        if check1:
            return dist1
        else:
            dist3 = readDist(frame, 32, 56, 336, 374, distConfig, False)

            check3 = (dist1 == dist3 or dist2 == dist3) and dist3 != -1 and dist3 < 100

            if check3:
                return dist3
            else:
                frame = frame[25:65, 330:380]
                frameVec = frame.flatten()
                if sum(frameVec) > 175000:
                    return 0
                elif sum(frameVec) > 168000:
                    return 0.5
                else:
                    pass


    path = "ScreenStuff/images/failedImages/" + computer[-3:] + "_distance_" + str(random.randint(1, 5)) + ".png"
    cv2.imwrite(path, frame)
    return -1

#frame = cv2.imread("ScreenStuff/images/comp4Images/40.png")
#frame = cv2.resize(frame, (1200, 800))
#print(getDistance(frame, "152.1.138.159"))
