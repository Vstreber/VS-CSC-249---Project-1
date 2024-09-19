# VS-CSC-249---Project-1


###   This is a simple word encoder/decoder client-server program. Here's how to use it!

    1. Input your desired effect on a word, either 'encode' or 'decode'. You can only decode a word 
       once you've encoded it, and you must know the CODE NUMBER to do so.

    2. Input your word. No spaces, numbers, special characters, or capitalization. Must be one word.

    3. Input your secret CODE NUMBER of choice. This is can be any positive number below 26, and it will allow 
       you to decode your word later.
   
####   Example input: 
   $ python client.py encode myword 6

##   Client-Server Message Format
In this program, the client has jurisdiction over the following:
- Handling misinputs/giving additional instruction
- Verifying initial connectivity with server (reports IP and port #)
- Gives information on sent and received information:
  - shows user that their request has been sent by repeaating it back to them
  - reports once each component of request has been individually sent
- For every RPC connecting to this project's server component, so long as three inputs are provided in the format of [encode/decode][word][number < 26], the server will respond as expected. So long as connection is secure (correct port/IP used), edits to text interface/data send within those bounds shouldn't cause issue.

The server has jurisdiction over the following:
- Reporting receival of command, message, and codenum from client
- Enacting the desired command using functions.py
  - More functions can easily be added to functions.py -- however, both client and server would have to be edited, as the client currently denies any command that isn't either Encode or Decode (as a half-baked way to prevent misinput)
- Sending data back to client
- So long as the server is able to receive inputs in the format of [command][word][number], edits can be made without causing issue. 

## Command Line Trace

CLIENT:

```$ python client.py encode networks 25
client starting - connecting to server at IP 127.0.0.1 and port 65432
Connection established. Sending the following request to server: 'encode the word networks using CODE NUMBER 25'
  > Command 'encode' sent.
  > Word 'networks' sent.
  > Code # '25' sent.
Waiting for reply...
Received response: 'networks' --> 'mdsvnqjr' [8 bytes]
Client is done!
```

SERVER:

```$ python server.py
server starting - listening for connections at IP 127.0.0.1 and port 65432
Connected established with ('127.0.0.1', 63443)
Received client command: 'b'encode'' [6 bytes]
Received client message: 'b'networks'' [8 bytes]
Received client codenum: 'b'25'' [2 bytes]
Sending altered message to client.
The encoded word is: 'mdsvnqjr'
Server is done!
```
