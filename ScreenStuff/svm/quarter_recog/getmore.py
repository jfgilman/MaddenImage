
import cv2

for i in range(2, 50):
    frame = cv2.imread("ScreenStuff/images/comp4Images/" + str(i) + ".png")
    frame = cv2.resize(frame, (1200, 800))

    frame = frame[25:65, 710:760]

    cv2.imwrite("quarter" + str(i) + ".png", frame)
