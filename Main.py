from functions import startup, formations2Player, formations1Player
from RasPi.RasPi import RasPi


def main():
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

    game_count = 0

    while True:
        formations2Player.play(home_pi, away_pi, controller, monitor)

        game_count += 1

        if game_count == num_games:
            home_pi.quitGame()
            break
        else:
            home_pi.restartGame()


def onePlayer(home_ip, from_scratch):
    pi = RasPi(host = home_ip, port = 5560)

    if from_scratch == "y":
        pi.startup()

    game_count = 0

    while True:
        formations1Player.play(home_pi, controller, monitor)

        game_count += 1

        if game_count == num_games:
            home_pi.quitGame()
            break
        else:
            home_pi.restartGame()


if __name__ == '__main__':
    main()
