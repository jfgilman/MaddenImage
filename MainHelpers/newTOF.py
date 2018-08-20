def callTimeout(gameState):

    scoreDiff = gameState['homeScore'] - gameState['awayScore']

    if gameState['quarter'] in [1, 3] or gameState['secsLeft'] > 120 or gameState['HomeTOR'] == 0:
        return False

    # First Half
    elif gameState['quarter'] == 2:
        if gameState['HomeOnOff']:
            if gameState['down'] < 4 and gameState['YTEZ'] < 60:
                return True
            elif gameState['down'] == 4 and gameState['YTEZ'] < 35:
                return True
            else:
                return False
        elif gameState['down'] > 2 and gameState['YTEZ'] > 70:
            return True
        else:
            return False

    # Second Half
    elif gameState['quarter'] == 4:
        if scoreDiff > 3:
            return False
        elif scoreDiff < 4 and scoreDiff > -1:
            if gameState['HomeOnOff']:
                return False
            elif gameState['YTEZ'] > 30:
                return False
            elif gameState['secsLeft'] < 30:
                return False
            else:
                return True
        elif scoreDiff > -4 and gameState['YTEZ'] < 30 and gameState['secsLeft'] > 40:
            return False
        else:
            return True

    # Overtime
    elif gameState['quarter'] == 5:
        if not gameState['HomeOnOff']:
            return False
        else:
            if gameState['YTEZ'] < 65 and gameState['down'] < 4:
                return True
            elif gameState['YTEZ'] < 35 and gameState['down'] == 4:
                return True
            else:
                return False
