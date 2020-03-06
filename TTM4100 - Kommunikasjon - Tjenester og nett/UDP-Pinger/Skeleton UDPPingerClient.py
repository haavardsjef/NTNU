import time
from socket import *

# Get the server hostname and port as command line arguments
host = "localhost"
port = 12000
timeout = 1

# Create UDP client socket
clientsocket = socket(AF_INET, SOCK_DGRAM)

# Set socket timeout as 1 second
clientsocket.settimeout(timeout)

# Sequence number of the ping message
ptime = 0

# Ping for 10 times
while ptime < 10:
    ptime += 1
    # Format the message to be sent as in the Lab description
    data = "PING: " + str(ptime) + " TIME: "

    try:
        # Record the "sent time"
        sent_time = time.time()
        asc_time = time.asctime()
        data += str(asc_time)

        # Send the UDP packet with the ping message
        clientsocket.sendto(data.encode(), (host, port))

        # Receive the server response
        message, clientadress = clientsocket.recvfrom(2048)

        # Record the "received time"
        recieved_time = time.time()

        # Display the server response as an output
        print()
        print("Server response: " + message.decode())
        # Calculate round trip time
        rt_time = recieved_time - sent_time
        # Display round trip time
        print("Round trip time:", rt_time)
        print()
        print("-----")
    except:
        # Server does not respond
        # Assume the packet is lost
        print("Request timed out.")
        print("-----")
        continue

# Close the client socket
clientsocket.close()
