import socket
import random

def tcpServer():

    # Initializing TCP connection and binding to port 17
    ts = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ts.bind(("localhost", 17))
    ts.listen()

    print("TCP Server initialized. Listening for connections on port 17")

    # Connect to client and send out a short welcome message
    # Then send out a random QOTD then shut down connection
    while True:
        cs, address = ts.accept()
        print(f"TCP connected with {address}")
        cs.send("You have been connected to the QOTD Server!".encode())

        # Choosing a quote from the server's list of quotes in random
        # and sending it to the client
        quote = quotes[random.randint(0, len(quotes)-1)]
        print(quote)
        cs.send(quote.encode())
        cs.close()

def udpServer():
    #Initializing UDP connection and binding to port 17
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as us:

      us.bind(("localhost", 17))

      print("UDP Server initialized, Listening for connections on port 17")

      # Connect to client and send out a short welcome message
      # Then send out a random QOTD then shut down connection
      while True:
        data, address = us.recvfrom(1024)
        print(f"UDP connected with {address}, {data.decode()} received")
        us.sendto("You have been connected to the QOTD Server!".encode(), address)

        #Choose a random quote from the server's list of quotes and send it to client
        quote = quotes[random.randint(0, len(quotes)-1)]
        us.sendto(quote.encode(), address)

quotes = ["If we burn, you burn with us -Random Quote",
          "I am your father -Starwars",
          "May the force be with you -Starwars",
          "You were the chosen one",
          "I am the one with the Force, and the Force is with me -Starwars",
          "As you wish -Starwars",
          "Is this a kissing book? -The Princess Bride",
          "I would not say such things if I were you! -The Princess Bride",
          "inconceivable -The Princess Bride",
          "After all this time? Always -Harry Potter",
          "Dobby is Free -Harry Potter",
          "Not my daughter, you bitch! -Harry Potter"
          ]

type = input("Which connection would you like, TCP or UDP ")
type = type.upper()
while type != 'TCP' and type != 'UDP':
  type = input("You can only choose between TCP and UDP (case insensitive) ").upper()

if type == "TCP":
  tcpServer()
if type == "UDP":
  udpServer()

