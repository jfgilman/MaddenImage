from functions import startup
from RasPi.RasPi import RasPi

(home_ip, home_team, away_ip, away_team, difficulty, controller,
monitor, from_scratch, num_games, qtr_length) = startup.getInfo()

home_pi = RasPi(host = home_ip, port = 5560)
away_pi = RasPi(host = away_ip, port = 5560)
