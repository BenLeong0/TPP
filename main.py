import socket

SERVER = "irc.twitch.tv"
PORT = 6667
PASS = "oauth:n6ehqgow73yltxti7y501ysj0irttz"
BOT = "npBot"
CHANNEL = "nopressure2"
OWNER = "nopressure2"
irc = socket.socket()
irc.connect((SERVER, PORT))
irc.send(("PASS " + PASS + "\n" +
          "NICK " + BOT + "\n" +
          "JOIN #" + CHANNEL + "\n").encode())

def joinchat():
    Loading = True
    while Loading:
        readbuffer_join = irc.recv(1024)
        readbuffer_join = readbuffer_join.decode()
        for line in readbuffer_join.split("\n"):
            print(line)
            Loading = loadingComplete(line)

def loadingComplete(line):
    if ("End of /NAMES list" in line):
        print("Bot has joined " + CHANNEL + "'s Channel!'")
        return False
    else:
        return True

joinchat()
