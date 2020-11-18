from socket import *
import time

# SERVER
mailserver = "smtp.csus.edu" 
serverPort = 25

# CLIENT
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver,serverPort))
recv = clientSocket.recv(1024).decode()
print(recv)

# HELO
heloCommand = "HELO Alice\r\n"
clientSocket.send(heloCommand.encode())
recv = clientSocket.recv(1024).decode()
print(recv)

# MAIL FROM
mailfromCommand = "MAIL FROM:jpoe@skynet.com\r\n"
clientSocket.send(mailfromCommand.encode())
recv = clientSocket.recv(1024).decode()
print(recv)

# RCPT TO
rcptTo = "RCPT TO:jpoe@skynet.com\r\n"
clientSocket.send((rcptTo).encode())
recv = clientSocket.recv(1024).decode()
print(recv)

# DATA
dataCommand = "DATA\r\n"
clientSocket.send((dataCommand).encode())
recv = clientSocket.recv(1024).decode()
print(recv)

# COMPOSE EMAIL
subject = "Subject: Bits OF real Panther\r\n\r\n" 
msg = "\r\n THIS IS NOT AN EMAIL!"
endmsg = "\r\n.\r\n"
date = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())
date = date + "\r\n\r\n"

# SEND
clientSocket.send(subject.encode())
clientSocket.send(date.encode())
clientSocket.send(msg.encode())
clientSocket.send(endmsg.encode())

# RECIEVE
recv = clientSocket.recv(1024).decode()
print(recv)

# QUIT
quit = "QUIT\r\n"
clientSocket.send(quit.encode())
recv = clientSocket.recv(1024).decode()
print(recv)
clientSocket.close()

