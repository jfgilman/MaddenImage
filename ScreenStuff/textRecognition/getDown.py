from PIL import Image
import pytesseract
import cv2
import random


def readDown(frame, row1, row2, col1, col2, config, showMe):
    # Slice the image according to the area of the image given
    downFrame = frame[row1:row2, col1:col2]

    # Resize the sliced image into a large box
    downFrame = cv2.resize(downFrame, (100, 100))

    # Shows the image if desired
    if showMe:
        cv2.imshow('Down Slice', downFrame)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    # Converts the image to a tesseract-compatible version
    tessFrame = Image.fromarray(downFrame)

    # Reads the down from the sliced image if possible
    try:
        down = pytesseract.image_to_string(tessFrame, config = config)[0]
    except:
        down = 0

    # Convert down to an integer if possible
    try:
        down = int(down)
    except:
        down = 0

    return down



def getDown(frame, computer):
    """
    Uses tesseract to classify the down in the given frame

    Args:
        frame: OpenCV image
            Current frame of the game
        computer: str
            ID of the computer the frame was taken from

    Returns: int
        Down from 1 to 4
    """

    # Convert the frame to gray                                                 TODO is this needed
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    # Configuration for tesseract to read only 1-4
    downConfig = "--psm 10000 -c tessedit_char_whitelist=1234"

    if computer == "152.1.138.157":
        down1 = readDown(frame, 25, 65, 305, 350, downConfig, False)
        down2 = readDown(frame, 30, 55, 300, 345, downConfig, False)
        #print(down1, down2)

        check1 = down1 == down2 and down1 != 0

        if check1:
            return down1
        else:
            down3 = readDown(frame, 32, 58, 305, 340, downConfig, False)
            #print(down3)

            check3 = (down1 == down3 or down2 == down3) and down3 != 0

            if check3:
                return down3
            else:
                down4 = readDown(frame, 32, 55, 302, 347, downConfig, False)
                #print(down4)

                check4 = (down1 == down4 or down2 == down4 or down3 == down4) and down4 != 0

                if check4:
                    return down4
                else:
                    pass
    elif computer == "152.1.138.158":
        down1 = readDown(frame, 25, 65, 305, 350, downConfig, False)
        down2 = readDown(frame, 30, 55, 300, 345, downConfig, False)
        #print(down1, down2)

        check1 = down1 == down2 and down1 != 0

        if check1:
            return down1
        else:
            down3 = readDown(frame, 32, 58, 305, 340, downConfig, False)
            #print(down3)
            check3 = (down1 == down3 or down2 == down3) and down3 != 0

            if check3:
                return down3
            else:
                down4 = readDown(frame, 30, 60, 305, 350, downConfig, False)
                #print(down4)

                check4 = (down4 == down1 or down4 == down2 or down4 == down3) and down4 != 0
                if check4:
                    return down4
    elif computer == "152.1.138.160":
        down1 = readDown(frame, 25, 65, 305, 350, downConfig, False)
        down2 = readDown(frame, 30, 55, 300, 345, downConfig, False)
        #print(down1, down2)

        check1 = down1 == down2 and down1 != 0

        if check1:
            return down1
        else:
            down3 = readDown(frame, 32, 58, 305, 340, downConfig, False)
            #print(down3)

            check3 = (down1 == down3 or down2 == down3) and down3 != 0

            if check3:
                return down3
            else:
                down4 = readDown(frame, 30, 55, 300, 347, downConfig, False)
                #print(down4)

                check4 = (down1 == down4 or down2 == down4 or down3 == down4) and down4 != 0

                if check4:
                    return down4
                else:
                    pass
    elif computer == "152.1.138.159":
        down1 = readDown(frame, 25, 65, 305, 350, downConfig, False)
        down2 = readDown(frame, 30, 55, 300, 345, downConfig, False)

        check1 = down1 == down2 and down1 != 0

        if check1:
            return down1
        else:
            down3 = readDown(frame, 32, 58, 305, 340, downConfig, False)

            check3 = (down1 == down3 or down2 == down3) and down3 != 0

            if check3:
                return down3
            else:
                pass
    else:
        down1 = readDown(frame, 25, 65, 305, 350, downConfig, False)
        down2 = readDown(frame, 30, 55, 300, 345, downConfig, False)

        check1 = down1 == down2 and down1 != 0

        if check1:
            return down1
        else:
            down3 = readDown(frame, 32, 58, 305, 340, downConfig, False)

            check3 = (down1 == down3 or down2 == down3) and down3 != 0

            if check3:
                return down3
            else:
                pass


    path = "ScreenStuff/images/failedImages/" + computer[-3:] + "_down_" + str(random.randint(1, 5)) + ".png"
    cv2.imwrite(path, frame)
    return -1

# frame = cv2.imread("ScreenStuff/images/failedImages/160_down_5.png")
# frame = cv2.resize(frame, (1200, 800))
# print(getDown(frame, "152.1.138.160"))
