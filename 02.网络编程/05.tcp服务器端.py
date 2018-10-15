from socket import *


serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('', 2333))

serverSocket.listen(5)

clientSocket, clientInfo = serverSocket.accept()

recvData = clientSocket.recv(1024)

print(f'{recvData} sent from ({str(clientInfo)})')

clientSocket.close()

serverSocket.close()