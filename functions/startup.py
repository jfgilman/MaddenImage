import sys
import Controller as C

def getInfo():
    num_players = input("Number of players: ")

    if num_players not in ("1", "2"):
        sys.exit("Only 1 or 2 players supported.")

    home_computer = input("Home Team -- pi Computer (LL_): ")

    if home_computer not in ("1", "2", "3", "4", "6", "7", "8", "9"):
        sys.exit("Please enter a valid computer number.")

    home_ip = None
    if home_computer == "1":
        home_ip = "152.1.138.157"
    elif home_computer == "2":
        home_ip = "152.1.138.158"
    elif home_computer == "3":
        home_ip = "152.1.138.160"
    elif home_computer == "4":
        home_ip = "152.1.138.159"
    elif home_computer == "6":
        home_ip = "192.168.1.14"
    elif home_computer == "7":
        home_ip = "192.168.1.18"
    elif home_computer == "8":
        home_ip = "192.168.1.24"
    elif home_computer == "9":
        home_ip = "192.168.1.30"

    home_team = "Chiefs"

    away_ip = None
    if num_players == "2":
        away_computer = input("Away Team -- pi Computer (LL_): ")

        if away_computer not in ("1", "2", "3", "4", "6", "7", "8", "9"):
            sys.exit("Please enter a valid computer number.")

        away_ip = None
        if away_computer == "1":
            away_ip = "152.1.138.157"
        elif away_computer == "2":
            away_ip = "152.1.138.158"
        elif away_computer == "3":
            away_ip = "152.1.138.160"
        elif away_computer == "4":
            away_ip = "152.1.138.159"
        elif away_computer == "6":
            away_ip = "192.168.1.14"
        elif away_computer == "7":
            away_ip = "192.168.1.18"
        elif away_computer == "8":
            away_ip = "192.168.1.24"
        elif away_computer == "9":
            away_ip = "192.168.1.30"

    away_team = input("Away Team: ")

    difficulty = "All-Pro"

    controller = C.randomPlay()

    monitor = None
    if home_computer in ("1", "2", "3"):
        monitor = "1"
    elif home_computer in ("4"):
        monitor = "2"
    else:
        monitor = "3"

    from_scratch = input("Currently on play now screen? ")
    if from_scratch.lower() not in ("y", "n"):
        sys.exit("Please give a valid answer.")

    num_games = 100

    qtr_length = 8

    return (home_ip, home_team, away_ip, away_team, difficulty, controller,
            monitor, from_scratch, num_games, qtr_length)
