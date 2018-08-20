import socket
import time


formations = {"34": 4, "43": 1, "46": 3, "dime": 6, "goallined": 7,
              "nickel": 5, "quarter": 2, "speciald": 8, "singleback": 1,
              "strong": 2, "weak": 3, "pistol": 4, "iform": 5, "gun": 6,
              "hailmary": 7, "goallineo": 8, "specialo": 9}


class RasPi(object):
    """
    Client class that connects to the RasPi server
    Has methods to send and receive messages, close the connection,
    and get and execute appropriate button presses

    Attr:
        host: string
            IP adress of Raspi server
        port: int
            Port address for the connection
        s: socket
            Socket created to send/receive information
    """
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.host, self.port))
        print("Connected to RasPi ", self.host)

    def send(self, command):
        """
        Sends a command to the server

        Args:
            command: string
                The string with the appropriate command
        Returns: void
        """
        self.s.send(str.encode(command))

    def receive(self):
        """
        Receives a command from the server

        Returns: void
        """
        reply = self.s.recv(1024)
        print(reply.decode('utf-8'))

    def close(self):
        """
        Close the connection with the server

        Returns: void
        """
        self.s.close()

    def callMadden(self, playType):
        """
        Execute the appropriate button presses for the ask madden bot

        Returns: void
        """
        if playType == "offense":
            self.send("Press A")
            time.sleep(13)
            self.send("Press A")
        elif playType == "defense":
            self.send("Press A")
            time.sleep(13)
            self.send("Press A")

    def callPlay(self, currentForm, formNum, setNum, button, playType, flip):
        """
        Execute the button sequence to call the correct playCall

        Args:
            currentForm: string
                The current formation the cursor is on.
            formNum: int
                The formation number of the play to be called
            setNum: int
                The set number of the play to be called
            button: Button
                The button of the play to be called
        Returns: void
        """

        currentFormNum = formations[currentForm]
        if(formNum < currentFormNum):
            for i in range(currentFormNum - formNum):
                self.send("Press UP")
                time.sleep(0.5)
        elif (currentFormNum < formNum):
            for i in range(formNum - currentFormNum):
                self.send("Press DOWN")
                time.sleep(0.5)
        for i in range(setNum - 1):
            self.send("Press RIGHT")
            time.sleep(0.5)
        self.send("Press A")
        time.sleep(1.5)
        if flip == 1:
            self.send("Press Y")
            time.sleep(1)
        self.send("Press " + button)
        # if playType == "offense":
        #     #self.send("Press A")
        #     time.sleep(8)
        #     self.send("Press A")
        #     print("SNAP")
        # elif playType == "defense" or playType == "kickoff":
        #     #self.send("Press A")
        #     pass

    def callTimeout(self):
        self.send("Press START")
        time.sleep(6)
        self.send("Press RIGHT")
        time.sleep(2)
        self.send("Press A")

    def kick(self, direction, difficulty):
        """
        Kick the ball

        Returns: void
        """
        if difficulty == "Rookie":
            if direction == "center":
                self.send("Press A")
                time.sleep(1.49)
                self.send("Press A")
                time.sleep(1.9)
                self.send("Press A")
                print("Kick Rookie Center")
            elif direction == "right":
                self.send("Press A")
                time.sleep(1.49)
                self.send("Press A")
                time.sleep(2.1)
                self.send("Press A")
            else:
                self.send("Press A")
                time.sleep(1.49)
                self.send("Press A")
                time.sleep(1.7)
                self.send("Press A")
        elif difficulty == "Pro":
            if direction == "center":
                self.send("Press A")
                time.sleep(1.09)
                self.send("Press A")
                time.sleep(1.47)
                self.send("Press A")
                print("KICK CENTER")
            elif direction == "right":
                self.send("Press A")
                time.sleep(1.09)
                self.send("Press A")
                time.sleep(1.62)
                self.send("Press A")
                print("KICK FROM RIGHT HASH")
            else:
                self.send("Press A")
                time.sleep(1.09)
                self.send("Press A")
                time.sleep(1.32)
                self.send("Press A")
                print("KICK FROM LEFT HASH")
        elif difficulty == "All Madden":
            if direction == "center":
                self.send("Press A")
                time.sleep(0.80)
                self.send("Press A")
                time.sleep(1.20)
                self.send("Press A")
            elif direction == "right":
                self.send("Press A")
                time.sleep(0.80)
                self.send("Press A")
                time.sleep(1.25)
                self.send("Press A")
            else:
                self.send("Press A")
                time.sleep(0.80)
                self.send("Press A")
                time.sleep(1.15)
                self.send("Press A")
        else:
            if direction == "center":
                self.send("Press A")
                time.sleep(0.94)
                self.send("Press A")
                time.sleep(1.25)
                self.send("Press A")
            elif direction == "right":
                self.send("Press A")
                time.sleep(0.94)
                self.send("Press A")
                time.sleep(1.35)
                self.send("Press A")
            else:
                self.send("Press A")
                time.sleep(0.94)
                self.send("Press A")
                time.sleep(1.15)
                self.send("Press A")

    def startUp(self):
        """
        Execute the button presses to start a game from play now screen
        Ensures correct xbox controller is being used

        Returns: void
        """
        self.send("Press A")
        time.sleep(1)
        self.send("Press A")
        time.sleep(10)
        self.send("Press A")

    def restartGame(self):
        """
        Execute the button presses to restart a game

        Returns: void
        """
        self.send("Press DOWN")
        time.sleep(2)
        self.send("Press RIGHT")
        time.sleep(2)
        self.send("Press A")
        time.sleep(2)
        self.send("Press DOWN")
        time.sleep(2)
        self.send("Press A")
        time.sleep(2)

    def quitGame(self):
        """
        Execute the button presses to quit the game upon completion

        Returns: void
        """
        self.send("Press DOWN")
        time.sleep(2)
        self.send("Press A")
        time.sleep(2)

    def getFinalScore(self):
        self.send("Press DOWN")
        time.sleep(2)
        self.send("Press RIGHT")
        time.sleep(2)
        self.send("Press RIGHT")
        time.sleep(2)
        self.send("Press A")
        time.sleep(15)

    def awayStartup(self):
        self.send("Press A")
        time.sleep(1)
        self.send("Press A")

    def homeStartup(self):
        self.send("Press A")
        time.sleep(1)
        self.send("Press A")
        time.sleep(10)
        self.send("Press A")
