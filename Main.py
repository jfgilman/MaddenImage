from MainHelpers import startup
from RasPi.RasPi import RasPi
from Game import Game
from datetime import datetime as dt
from MainHelpers import playGame
import pandas as pd

# Gather all the input information
(piIP, homeTeam, awayTeam, difficulty, controller,
fromScratch, numGames, quarterLength, bottomMonitor) = startup.getInfo()


# Setup Raspberry Pi connection and execute startup button presses if necessary
pi = RasPi(host=piIP, port=5560)
if fromScratch:
    pi.startUp()

gameCount = 0

while True:
    # Initialize the game variable
    game = Game(str(dt.now()), piIP, difficulty, controller, homeTeam,
                awayTeam, quarterLength)

    # Play the game
    awayFinal, homeFinal = playGame.play(pi, game, controller, bottomMonitor)
    gameCount += 1

    # Restart the game if necessary
    if gameCount == numGames:
        pi.quitGame()
        break
    else:
        pi.restartGame()
