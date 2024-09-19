import socket
import sys

HOST = "127.0.0.1"
PORT = 65432

# ---------------------------------------------------------------------------------------------------
#   This is a simple word encoder/decoder client-server program. Here's how to use it!
#
#    1. Input your desired effect on a word, either 'encode' or 'decode'. You can only decode a word 
#       once you've encoded it, and you must know the CODE NUMBER to do so.
#
#    2. Input your word. No spaces, numbers, special characters, or capitalization. Must be one word.
#
#    3. Input your secret CODE NUMBER of choice. This is can be any positive number, and it will allow 
#       you to decode your word later.
#   
#   Example input: 
#   $ python client.py encode myword 6
# ---------------------------------------------------------------------------------------------------

if len(sys.argv) != 4:
    print("\nPlease only provide three arguements: \n 1. The desired function ('encode' OR 'decode') \n 2. The single word to be encoded/decoded \n 3. The encryption number (must be positive)")
    print("\nEXAMPLE INPUT: \n $ python client.py encode myword 6")
elif (sys.argv[1] != 'encode') and (sys.argv[1] != 'decode'):
    print("\nPlease ensure that your command (first word entered) is either 'encode' or 'decode'.")
    print("\nEXAMPLE INPUT: \n $ python client.py encode myword 6")
elif (sys.argv[2].isalnum() != True) or (sys.argv[2].islower() != True):
    print("\nPlease ensure that your word (second word entered) only consists of lowercase alphabetical letters (a-z).")
    print("\nEXAMPLE INPUT: \n $ python client.py encode myword 6")
elif sys.argv[3].isnumeric() != True:
    print("\nPlease ensure that your code number (third word entered) is a positive number under 26.")
    print("\nEXAMPLE INPUT: \n $ python client.py encode myword 6")
elif (int(sys.argv[3]) < 0):
    print("\nPlease ensure that your code number (third word entered) is a positive number under 26.")
    print("\nEXAMPLE INPUT: \n $ python client.py encode myword 6")
else:
    COMMAND = sys.argv[1]
    MESSAGE = sys.argv[2]
    CODENUM = sys.argv[3]
    print("client starting - connecting to server at IP", HOST, "and port", PORT)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        s.connect((HOST, PORT))

        print(f"Connection established. Sending the following request to server: '{COMMAND} the word {MESSAGE} using CODE NUMBER {CODENUM}'")
        s.sendall(bytes(COMMAND, 'utf-8'))
        print("  > Command '" + COMMAND + "' sent.")
        data = s.recv(1024)

        s.sendall(bytes(MESSAGE, 'utf-8'))
        print("  > Word '" + MESSAGE + "' sent.")
        data = s.recv(1024)

        s.sendall(bytes(CODENUM, 'utf-8'))
        print("  > Code # '" + CODENUM + "' sent.")
        print("Waiting for reply...")

        data = s.recv(1024)

        dataString = str(data)
        dataString = dataString[2:-1]
        
        print(f"Received response: '{MESSAGE}' --> '{dataString}' [{len(data)} bytes]")


    print("Client is done!")