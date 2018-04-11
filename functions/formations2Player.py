import mss
import sys
import img

def play(home_pi, away_pi, controller, monitor):
    # Load screen type model that give "other", "playcall", "kickoff", or "endgame"

    with mss.mss() as sct:
        if monitor == "1":
            monitor = {'top': 0, 'left': 0, 'width': 3840, 'height': 2160}
        elif monitor == "2":
            monitor = {'top': -2160, 'left': 0, 'width': 3840, 'height': 2160}
        elif monitor == "3":
            monitor = {'top': 0, 'left': 0, 'width': 1280, 'height': 720}
        else:
            sys.exit("Invalid monitor number.")

    while True:
        screen_type = "other"

        while screen_type == "other":
            frame = img.prepFrame(sct, monitor)
