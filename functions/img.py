import numpy as np
import cv2


def prepFrame(sct, monitor, gray = False):
    frame = np.array(sct.grab(monitor))
    frame = cv2.resize(frame, (1200, 800))
    if gray:
        try:
            gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
            return gray
        except Exception:
            return "Bad Frame"
    else:
        return frame
