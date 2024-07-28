# Importing Libraries
import socket

# Create a client socket, request an IP from user, connection Attempt
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP_input = input("Enter an IP address that you wish to connect to: ")
client_socket.connect((IP_input, 8000))
# Receive & print greeting from server. Get the user's name, then print the game's instructions
print(client_socket.recv(2048).decode()) # Print greeting
client_socket.send(input("Enter your Name: ").encode())
print(client_socket.recv(2048).decode()) # Print game instructions

# Strings that indicate a final result (end of the game)
WIN = "Good Job"
LOSS = "Game Over!"
# Get a guess from user, send it to user. If the reply includes WIN or LOSS strings the game ended. Otherwise, try guessing again
while True:
    client_socket.send((input("")).encode())
    server_reply = client_socket.recv(2048).decode()
    print(server_reply)
    if (WIN in server_reply or LOSS in server_reply): break

# Closing the client socket
client_socket.close()