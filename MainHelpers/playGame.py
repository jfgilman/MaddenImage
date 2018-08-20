import pickle
from MainHelpers import imageFunctions as fn
# from MainHelpers import timeOutFunc as tof
from MainHelpers import newTOF as tof
from ScreenStuff.textRecognition.getFinalScore import getFinalScore
from ScreenStuff.textRecognition.getAskMaddenPlayName import getAskMaddenPlayName
import mss
import time
import random
import cv2

# Return the final score
def play(pi, game, controller, bottomMonitor):
    """
    Plays the game.

    args:
        pi: RasPi object
        game: Game object
        controller: Controller object

    returns:
        awayFinal: int
            Final score for the away team
        homeFinal: int
            Final score for the home team
    """

    # Load the models used in the script
    screenTypeModel = pickle.load(open("ScreenStuff/svm/game_state_recog/" +
                                       "finalized_game_state_model.sav", 'rb'))
    offFormModel = pickle.load(open("ScreenStuff/svm/formation_recog_off/" +
                                    "finalized_OffForm_model.sav", 'rb'))
    defFormModel = pickle.load(open("ScreenStuff/svm/formation_recog_def/" +
                                    "finalized_DefForm_model.sav", 'rb'))
    personnelModel = pickle.load(open("ScreenStuff/svm/personel_recog/" +
                                      "finalized_offPersonel_model.sav", 'rb'))
    filterModel = pickle.load(open("ScreenStuff/svm/filter_screen_recog/" +
                                   "finalized_FilterScreen_model.sav", 'rb'))

    with mss.mss() as sct:

        # Set the monitor size
        if bottomMonitor == "y":
            monitor = {'top': 0, 'left': 0, 'width': 3840, 'height': 2160}
        elif "192" in game.CPUID:
            monitor = {'top': 0, 'left': 0, 'width': 1280, 'height': 720}
        else:
            monitor = {'top': -2160, 'left': 0, 'width': 3840, 'height': 2160}

        while True:
            # Reset the stuckCount to 0 after every full iteration
            stuckCount = 0

            # Initialize/reset the screenType to "other"
            screenType = "other"
            clockRunningChecked = False

            while screenType == "other":
                # Increase the stuck count each iteration through the loop
                stuckCount = stuckCount + 1

                # Check if stuckCount is high. If so, hit A and reset the count
                stuckCount = fn.checkStuck(stuckCount, pi)

                # Grab and prepare a frame
                frame = fn.prepFrame(sct, monitor)

                # If grabbing the frame doesn't work, skip this iteration
                if frame == "Bad Frame":
                    continue

                # Get a gray version of the frame
                gray = fn.grayFrame(frame)

                # If graying the frame doesn't work, skip this iteration
                if gray == "Bad Frame":
                    continue

                # Use the gray image and screen type model to get screen type
                screenCheck = fn.getScreenType(gray, screenTypeModel)

                # If the screen type is "game over", get the final score
                if screenCheck == "end_game":
                    time.sleep(1)
                    pi.getFinalScore()
                    finalFrame = fn.prepFrame(sct, monitor)
                    finalFrame = fn.grayFrame(finalFrame)
                    pi.send("Press B")
                    time.sleep(2)
                    pi.send("Press B")
                    time.sleep(2)
                    return getFinalScore(finalFrame, game.state['homeScore'], game.state['awayScore'], game.CPUID)

                # If we have made it to a significant screen
                if screenCheck != "other":

                    # Prep images 1 second apart to see if the clock is running
                    checkFrame, trueFrame = fn.prepClockFrames(sct, monitor,
                                                               frame)

                    # If the image prep didn't work, skip this iteration
                    if checkFrame == "Bad Frame" or trueFrame == "Bad Frame":
                        continue

                    # Check if the clock is running
                    if not clockRunningChecked:
                        clockRunning = fn.checkClockRunning(checkFrame, trueFrame, game) #TODO fix that I'm resetting to false
                        clockRunningChecked = True
                        #print(clockRunningChecked)
                        #print(clockRunning)

                    # Confirm the screen was correctly labeled
                    screenType = fn.confirmScreenType(trueFrame, screenTypeModel)

                    # If we are on an offensive or defensive play call screen
                    if screenType == screenCheck:
                        if screenType != "otherTO":
                            if "192" in game.CPUID:
                                time.sleep(0.5)
                                trueFrame = fn.prepFrame(sct, monitor)
                            break
                        else:
                            screenType = "other"
                    else:
                        screenType = "other"
                        # continue

            ###################################################################
            ######################### ACTION SEQUENCE #########################
            ###################################################################

            # Check if we are on a kickoff to avoid updating the state
            if screenType == "kickoff":
                pi.send("Press A")
                time.sleep(7)
                pi.kick("center", game.difficulty)
                continue

            # Update the game state with the new frame's information
            game.updateState(trueFrame)

            #print(screenType)
            if screenType == "offense":
                game.updateHomeBall(True, trueFrame, game.state['AwayTOR'])
                personnel = "NICK"
                game.updateOffPersonnel(personnel)
            else:
                game.updateHomeBall(False, trueFrame, game.state['AwayTOR'])
                trueGray = fn.grayFrame(trueFrame)
                personnel = fn.getScreenType(trueGray[660:690, 175:280], personnelModel)
                game.updateOffPersonnel(personnel)


            # if clockRunning:
            #     if tof.callTimeout(game.state):
            #         pi.callTimeout()
            #         game.updateHomeTimeOuts()

            fn.defenseUpdates(screenType, gray, personnelModel, game)

            headline = "OTHER"
            #headline = fn.randomInitialize(sct, monitor, pi)

            while headline == "OTHER":
                stuckFrame = fn.prepFrame(sct, monitor)
                stuckFrame = fn.grayFrame(stuckFrame)
                currentScreen = fn.getScreenType(stuckFrame, screenTypeModel)
                if currentScreen == "end_game":
                    time.sleep(1)
                    return None, None                                          #TODO another place for final score implementation
                elif currentScreen == "kickoff":
                    pi.send("Press A")
                    time.sleep(7)
                    pi.kick("center", game.difficulty)
                    break
                elif currentScreen == "other":
                    time.sleep(1)
                    stuckFrame = fn.prepFrame(sct, monitor)
                    stuckFrame = fn.grayFrame(stuckFrame)
                    currentScreen = fn.getScreenType(stuckFrame, screenTypeModel)
                    if currentScreen == "other":
                        break

                headline = fn.otherReset(sct, monitor, pi)

            #try:
            playCall, fNum, sNum, button, pNum, flip = controller.getPlayCall(game.state) #TODO cont.getPlayCall(game.state)
            print("Play call: ", playCall)
                #print("Play number: ", pNum)
            #except:
                #playCall = "Ask Madden"

            if headline == "FILTER":
                filterFrame = fn.prepFrame(sct, monitor)
                filterFrame = fn.grayFrame(filterFrame)
                filterCursor = fn.getScreenType(filterFrame[120:570, 675:1130], filterModel)

                if playCall == "Ask Madden":
                    game.playCall = playCall
                    fn.navigateToAskMadden(filterCursor, pi)
                    kickType = fn.execAskMadden(sct, monitor, screenType, game, pi)
                    if kickType == "PUNT":
                        fNum = 9
                        sNum = 2
                        button = 'X'
                        pNum = 71
                    elif kickType == "FG":
                        fNum = 9
                        sNum = 1
                        button = 'X'
                        pNum = 68
                    else:
                        fNum = None
                        sNum = None
                        button = None
                        pNum = None
                    game.updatePlayStuff(kickType, fNum, sNum, button, pNum)              #TODO game.updatePlayStuff(playCall, fnum, ...)
                    game.appendData()
                else:
                    fn.navigateToFormation(filterCursor, pi)
                    headline = "FORMATION"

            if headline == "FORMATION":
                game.playCall = playCall
                if playCall == "Ask Madden":
                    pi.send("Press B")
                    time.sleep(1.5)
                    pi.send("Press UP")
                    time.sleep(0.5)
                    pi.send("Press A")
                    time.sleep(1.5)
                    kickType = fn.execAskMadden(sct, monitor, screenType, game, pi)
                    if kickType == "PUNT":
                        fNum = 9
                        sNum = 2
                        button = 'X'
                        pNum = 71
                    elif kickType == "FG":
                        fNum = 9
                        sNum = 1
                        button = 'X'
                        pNum = 68
                    else:
                        fNum = None
                        sNum = None
                        button = None
                        pNum = None
                    game.updatePlayStuff(kickType, fNum, sNum, button, pNum)
                    game.appendData()
                elif pNum == 68 or pNum == 71:
                    game.updatePlayStuff(playCall, fNum, sNum, button, pNum)
                    if pNum == 71:
                        game.playCall = "PUNT"
                    else:
                        game.playCall = "FG"
                    game.appendData()
                    pi.send("Press DOWN")
                    time.sleep(1)
                    formFrame = fn.prepFrame(sct, monitor)
                    formFrame = fn.grayFrame(formFrame)
                    formFrame = formFrame[120:660, 675:980]
                    if game.homeBall:
                        currentForm = fn.getScreenType(formFrame, offFormModel)
                    else:
                        currentForm = fn.getScreenType(formFrame, defFormModel)

                    pi.callPlay(currentForm, fNum, sNum, button, screenType)
                    time.sleep(8)
                    hashFrame = fn.prepFrame(sct, monitor)
                    direction = fn.hashCheck(hashFrame)
                    pi.kick(direction, game.difficulty)
                else:
                    game.updatePlayStuff(playCall, fNum, sNum, button, pNum)
                    game.appendData()
                    # pi.send("Press DOWN")
                    # time.sleep(1)
                    # formFrame = fn.prepFrame(sct, monitor)
                    # formFrame = fn.grayFrame(formFrame)
                    # formFrame = formFrame[120:660, 675:980]
                    #print(game.homeBall)
                    if game.homeBall:
                        currentForm = "singleback"
                        # currentForm = fn.getScreenType(formFrame, offFormModel)
                    else:
                        currentForm = "43"
                        # currentForm = fn.getScreenType(formFrame, defFormModel)

                    pi.callPlay(currentForm, fNum, sNum, button, screenType, flip)
                    if game.homeBall:
                        time.sleep(8)
                        #formationSnap(fNum, sNum, True, sct, monitor)
                        time.sleep(1)
                        formationFrame = fn.prepFrame(sct, monitor)
                        formationPath = "C://Temp/MaddenImage/ScreenStuff/images/formationImages/" + str(fNum) + "_" + str(sNum) + "_" + str(flip) + "_" + str(random.randint(0, 10000)) + ".png"
                        cv2.imwrite(formationPath, formationFrame)
                        time.sleep(5)
                        pi.send("Press A")
                    else:
                        time.sleep(5)
