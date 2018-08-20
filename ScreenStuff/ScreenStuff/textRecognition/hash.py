from PIL import Image
import pytesseract
import cv2

def hashCheck(frame):
    #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame1 = frame[400:430, 0:10]

    #frame1 = cv2.bitwise_not(frame1)
    frame1Vec = frame1.flatten()
    frame1VecSum = sum(frame1Vec)
    #print(frame1VecSum)
    cv2.imshow('frame', frame1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print(frame1VecSum)
    if frame1VecSum > 100000:
        ret = "left"
    # if ret == "left":
    #     frame2 = frame[400:432, 1191:1200]
    #     frame2 = cv2.bitwise_not(frame)
    #     frame2Vec = frame2.flatten()
    #     frame2VecSum = sum(frame2Vec)
    #     cv2.imshow('frame', frame2)
    #     cv2.waitKey(0)
    #     ret = "center"
    else:
        frame2 = frame[330:355, 0:10]
        frame2Vec = frame2.flatten()
        frame2VecSum = sum(frame2Vec)
        cv2.imshow('frame', frame2)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print(frame2VecSum)
        if frame2VecSum > 100000:
            ret = "center"
        else:
            ret = "right"
        #cv2.imshow('frame', frame2)
        #cv2.waitKey(0)
        #ret = "right"
        #frame = cv2.GaussianBlur(frame, (5, 5), 0)
    # thresh, frame = cv2.threshold(frame, 100, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 11, 2)
    # frame1 = cv2.resize(frame, (100,102))
    # frame2 = cv2.resize(frame, (200, 200)) #changed values
    # tessFrame = Image.fromarray(frame2)
    # ret = pytesseract.image_to_string(tessFrame, config="--psm 10000 -c tessedit_char_whitelist=0123456789")
    # cv2.imshow('frame', frame2)
    # cv2.waitKey(0)
    #cv2.destroyAllWindows()
    # if ret == "":
    #      #doesn't recognize 0 alone, so this is a measure to prevent that
    #     tessFrame = Image.fromarray(frame1)
    #     ret = pytesseract.image_to_string(tessFrame, config="--psm 10000 -c tessedit_char_whitelist=0123456789")
    #     cv2.imshow('frame1', frame1)
    #     cv2.waitKey(0)
    return(ret)

frame = cv2.imread("ScreenStuff/images/hashImages/30.png")
#frame = cv2.resize(frame, (1200, 800))
print(hashCheck(frame))
