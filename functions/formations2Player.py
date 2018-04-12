import mss
import sys
import img
import time

# TODO   line 12  : actual model needs to be loaded
# TODO end of file: action sequence needs to be written


def play(home_pi, away_pi, controller, monitor, difficulty):
    # Load screen type model that give "other","playcall","kickoff",or"endgame"
    screen_type_model = None

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
            frame = img.prepFrame(sct, monitor, gray = True)

            if frame == "Bad Frame":
                continue

            screen_check_1 = img.getPrediction(frame, screen_type_model)

            if screen_check_1 == "end_game":
                time.sleep(1)
                return None

            if screen_check_1 != "other":
                frame_2 = img.prepFrame(sct, monitor, gray = True)

                screen_check_2 = img.getPrediction(frame_2, screen_type_model)

                if screen_check_1 == screen_check_2:
                    break
                else:
                    screen_type = "other"

        if screen_check_2 == "kickoff":
            pi.send("Press A")
            time.sleep(7)
            pi.kick("center", difficulty)
            continue
