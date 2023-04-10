
import random 
from socket import*
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("server is ready to receive")
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode().upper() + " " + str(random.randint(0, 10)) + " is your lucky number to be selected"
   
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
    
    