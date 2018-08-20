def callTimeout(gameState):

    offense = gameState['HomeOnOff']
    TORemaining = gameState['HomeTOR']
    ourScore = gameState['homeScore']
    oppScore = gameState['awayScore']
    down = gameState['down']
    yardsToFirst = gameState['distance']
    yardsToTD = gameState['YTEZ']
    quarter = gameState['quarter']
    timeOnClock = gameState['secsLeft']
    scoreDiff = ourScore - oppScore

    if offense:
        if scoreDiff <= 0:
            if quarter == 2:
                if timeOnClock < 10:
                    if yardsToTD < 35:
                        return True
                    else:
                        return False
                elif timeOnClock < 120:
                    if yardsToTD > 40:
                        if TORemaining > 1:
                            if down == 4 and yardsToFirst > 2:
                                return True
                            else:
                                return False
                        else:
                            return False
                    else:
                        if TORemaining > 1:
                            return True
                        else:
                            return False
                else:
                    return False
            elif quarter == 4:
                if timeOnClock < 10:
                    return True
                elif timeOnClock < 120:
                    if yardsToTD > 40:
                        if TORemaining > 1:
                            if down == 4 and yardsToFirst > 1:
                                return True
                            else:
                                return False
                        else:
                            return False
                    else:
                        if TORemaining > 1:
                            return True
                        else:
                            return False
                else:
                    return False
            else:
                return False
        else:
            if quarter == 2:
                if timeOnClock < 10:
                    if yardsToTD < 35:
                        return True
                    else:
                        return False
                elif timeOnClock < 120:
                    if yardsToTD > 40:
                        if TORemaining > 1:
                            if down == 4 and yardsToFirst > 2:
                                return True
                            else:
                                return False
                        else:
                            return False
                    else:
                        if TORemaining > 1:
                            return True
                        else:
                            return False
                else:
                    return False
            else:
                return False
    else:
        if quarter == 2 or quarter == 4:

            if TORemaining == 3:
                if scoreDiff > 8:
                    return False
                elif scoreDiff <= 8 and scoreDiff > 3:
                    if yardsToTD < 30 and timeOnClock < 180:
                        return True
                    else:
                        return False
                elif scoreDiff <= 3 and scoreDiff >= 0:
                    if yardsToTD < 35 and timeOnClock < 180:
                        return True
                    else:
                        return False
                else:
                    if timeOnClock < 180:
                        return True
                    else:
                        return False
            elif TORemaining == 2:
                if scoreDiff > 8:
                    return False
                elif scoreDiff <= 8 and scoreDiff > 3:
                    if yardsToTD < 30 and timeOnClock < 120:
                        return True
                    else:
                        return False
                elif scoreDiff <= 3 and scoreDiff >= 0:
                    if yardsToTD < 35 and timeOnClock < 120:
                        return True
                    else:
                        return False
                else:
                    if timeOnClock < 120:
                        return True
                    else:
                        return False
            elif TORemaining == 1:
                if scoreDiff > 8:
                    return False
                elif scoreDiff <= 8 and scoreDiff > 3:
                    if yardsToTD < 30 and timeOnClock < 90:
                        return True
                    else:
                        return False
                elif scoreDiff <= 3 and scoreDiff >= 0:
                    if yardsToTD < 35 and timeOnClock < 90:
                        return True
                    else:
                        return False
                else:
                    if timeOnClock < 90:
                        return True
                    else:
                        return False
            else:
                return False
        else:
            return False
