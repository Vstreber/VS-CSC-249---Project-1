import sys

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encode(MESSAGE, CODENUM):

    CODENUM = int(CODENUM)
    encodedWord = ''
    iterator = 0
    letterIndex = [alphabet.index(i) for i in MESSAGE]

    for i in letterIndex:
        if (i + CODENUM) > 25:
            difference = 26 - i
            encodedWord = encodedWord + alphabet[CODENUM - difference]
            iterator+=1
        else:
            encodedWord = encodedWord + alphabet[letterIndex[iterator] + CODENUM]
            iterator+=1

    print("The encoded word is: '" + encodedWord + "'")
    return (bytes(encodedWord, 'utf-8'))

def decode(MESSAGE, CODENUM):

    CODENUM = int(CODENUM)
    decodedWord = ''
    iterator = 0
    letterIndex = [alphabet.index(i) for i in MESSAGE]

    for i in letterIndex:
        if (i - CODENUM) < 26:
            difference = CODENUM - i
            decodedWord = decodedWord + alphabet[26-difference]
            iterator+=1
        else:
            decodedWord = decodedWord + alphabet[letterIndex[iterator] - CODENUM]
            iterator+=1

    print("The decoded word is: '" + decodedWord + "'")
    return (bytes(decodedWord, 'utf-8'))
