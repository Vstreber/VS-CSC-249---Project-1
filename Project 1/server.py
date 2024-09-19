from functions import *
import socket

HOST = "127.0.0.1" 
PORT = 65432 
COMMAND = ''
MESSAGE = ''
CODENUM = ''

print("server starting - listening for connections at IP", HOST, "and port", PORT)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected established with {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
        
            dataString = str(data)
            dataString = dataString[2:-1]

            if dataString == 'encode' or dataString == 'decode':
                COMMAND = dataString
                print(f"Received client command: '{data!r}' [{len(data)} bytes]")
            elif dataString.isnumeric() == True:
                CODENUM = dataString
                print(f"Received client codenum: '{data!r}' [{len(data)} bytes]")
            else:
                MESSAGE = dataString
                print(f"Received client message: '{data!r}' [{len(data)} bytes]")

            if (COMMAND != '') & (MESSAGE!= '') & (CODENUM != ''):
                print("Sending altered message to client.")
                conn.sendall(globals()[COMMAND](MESSAGE,CODENUM))
            else:
                conn.sendall(data)


print("Server is done!")
