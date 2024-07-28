# Importing libraries
import random
import socket

"""
Function: IS_GUESS_CORRECT - Checks if guess a is correct.
IS_GUESS_CORRECT receives- Client, Clients name, Clients current guess, Number generated (answer), Current turn.
IS_GUESS_CORRECT returns- True/False if guess is correct/incorrect.
"""
def IS_GUESS_CORRECT(client, client_name, client_guess, answer, current_turn):
    if (client_guess == answer): # Correct Guess
        print("The player {0} won in {1} tries!\nDisconnecting...".format(client_name, current_turn))
        client.send(("Good Job, {0}!\nYou guessed my number in {1} guesses".format(client_name, current_turn)).encode())
        return True
    if (client_guess != answer and current_turn == 5): # Incorrect Guess and no tries left
        print("The player {0} has lost!\nDisconnecting...".format(client_name))
        client.send(("Game Over!\nThe number I had in my mind was actually {0}\nBetter luck next time!".format(answer)).encode())
        return False
    client.send(("Your guess is too {0}!\nTries left: {1}\nTake a guess.".format("low" if client_guess < answer else "high", 5 - current_turn)).encode())
    return False

# Creating server socket, waiting for a single connection
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("", 8000))
server_socket.listen(1)
print("Waiting for a player...")
# Accepting connection, printing connection status
(client, (ip, port)) = server_socket.accept()
print("Connection established at address {0} and at port {1}".format(ip, port))
# Get information from client, then send him the instructions
client.send("Welcome to guess the number!\nWhat is your name?".encode())
client_name = client.recv(2048).decode()
instructions = "Well {0}, I am thinking of a number between 1 and 20.\nYou have 5 tries to guess the number.\nGood luck!\nTake a guess.".format(client_name)
client.send(instructions.encode())

# Initializing variables of the game
current_try = 1
generated_number = random.randint(1, 20)
# While client has tries left - check if received guess is correct. If correct - end game (break loop), else - continue to guess.
while current_try < 6:
    current_guess = int(client.recv(2048).decode())
    if (IS_GUESS_CORRECT(client, client_name, current_guess, generated_number, current_try)): break
    current_try += 1

# Game finished - closing server connection. Client won or reached maximum tries and lost
server_socket.close()