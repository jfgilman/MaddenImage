import sys
import Controller as C
import unittest


def getInfo():
    """
    Prompts the user to input all the necessary information for the game.

    Args:
        void

    Returns:
        piIP: string
            IP address of the Raspberry Pi for connection
        homeTeam: string
            Home team in the game
        awayTeam: string
            Away team in the game
        difficulty: string
            Difficulty selected for the game
        controller: Controller
            Controller to be used for the game
        fromScratch: bool
            Whether or not the game is on the "Play Now" screen
        numGames: int
            Number of games to be played if uninterrupted
        quarterLength: int
            Length of the quarters in these games
    """
    default = input("Default settings (y/n): ")
    if default.lower() not in ("y", "n"):
        sys.exit("Please give a valid answer.")
    elif default == "y":
        computer = input("Computer (LL_): ")
        piIP = None
        if computer not in ("1", "2", "3", "4", "6", "7", "8", "9"):
            sys.exit("Please enter a valid computer number.")
        elif computer == "1":
            piIP = "152.1.138.157"
        elif computer == "2":
            piIP = "152.1.138.158"
        elif computer == "3":
            piIP = "152.1.138.160"
        elif computer == "4":
            piIP = "152.1.138.159"
        elif computer == "6":
            piIP = "192.168.1.14"
        elif computer == "7":
            piIP = "192.168.1.18"
        elif computer == "8":
            piIP = "192.168.1.24"
        else:
            piIP = "192.168.1.30"

        homeTeam = "Chiefs"

        awayTeam = input("Away Team: ")

        difficulty = "All-Pro"

        controller = "5"

        if computer in ("1", "2", "3"):
            bottomMonitor = "y"
        else:
            bottomMonitor = "n"

        fromScratch = input("Currently on play now screen: (y/n): ")
        if fromScratch.lower() not in ("y", "n"):
            sys.exit("Please give a valid answer.")

    else:
        computer = input("Computer (LL_): ")
        piIP = None
        if computer not in ("1", "2", "3", "4", "6", "7", "8", "9"):
            sys.exit("Please enter a valid computer number.")
        elif computer == "1":
            piIP = "152.1.138.157"
        elif computer == "2":
            piIP = "152.1.138.158"
        elif computer == "3":
            piIP = "152.1.138.160"
        elif computer == "4":
            piIP = "152.1.138.159"
        elif computer == "6":
            piIP = "192.168.1.14"
        elif computer == "7":
            piIP = "192.168.1.18"
        elif computer == "8":
            piIP = "192.168.1.24"
        else:
            piIP = "192.168.1.30"

        homeTeam = input("Home Team: ")

        awayTeam = input("Away Team: ")

        difficulty = input("Difficulty: \n 1 for Rookie \n 2 for Pro" +
                           "\n 3 for All-Pro \n 4 for All-Madden \n")
        if difficulty not in ("1", "2", "3", "4"):
            sys.exit("Please give a valid answer. (1, 2, 3, or 4)")

        controller = input("Controller: \n 1 for askMadden \n 2 for Random" +
                           "\n 3 for Random Texan \n 4 for Random Colt")

        if controller not in ("1", "2", "3", "4"):
            sys.exit("Please give a valid answer. (1, 2, 3, or 4)")


        bottomMonitor = input("Play on bottom monitor: (y/n): ")
        if bottomMonitor.lower() not in ("y", "n"):
            sys.exit("Please give a valid answer.")

        fromScratch = input("Currently on play now screen: (y/n): ")
        if fromScratch.lower() not in ("y", "n"):
            sys.exit("Please give a valid answer.")

    numGames = 100

    quarterLength = 8

    if difficulty == "1":
        difficulty = "Rookie"
    elif difficulty == "2":
        difficulty = "Pro"
    elif difficulty == "3":
        difficulty = "All-Pro"
    elif difficulty == "4":
        difficulty = "All-Madden"

    if controller == "1":
        controller = C.AskMadden()
    elif controller == "2":
        controller = C.randomPlay()
    elif controller == "3":
        controller = C.randomTexan()
    elif controller == "4":
        controller = C.randomColt()

    if fromScratch.lower() == "y":
        fromScratch = True
    else:
        fromScratch = False

    return (piIP, homeTeam, awayTeam, difficulty, controller, fromScratch,
            numGames, quarterLength, bottomMonitor)
