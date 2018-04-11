from functions import startup
from RasPi.RasPi import RasPi

(home_ip, home_team, away_ip, away_team, difficulty, controller,
monitor, from_scratch, num_games, qtr_length) = startup.getInfo()

if away_ip is not None:
    twoPlayer(home_ip, away_ip, from_scratch)
else:
    onePlayer()

def twoPlayer(home_ip, away_ip, from_scratch):
    home_pi = RasPi(host = home_ip, port = 5560)
    away_pi = RasPi(host = away_ip, port = 5560)

    if from_scratch == "y":
        away_pi.awayStartup()
        home_pi.homeStartup()


def onePlayer(home_ip, from_scratch):
    pi = RasPi(host = home_ip, port = 5560)

    if from_scratch == "y":
        pi.startup()
