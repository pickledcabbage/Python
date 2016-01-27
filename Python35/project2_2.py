# Project 2, Part 2

import connectfour
import Project2
import socket

def connectToAI(sc:socket):
    username = input('Enter your desired username: ')
    usermessage = 'I32CFSP_HELLO ' + username + '\r\n'
    sc.send(usermessage.encode(encoding='utf-8'))
    print(sc.recv(4096).decode(encoding = 'utf-8').rstrip())
    sc.send('AI_GAME\r\n'.encode(encoding = 'utf-8'))
    print(sc.recv(4096).decode(encoding='utf-8'))

def gameProcess():
    pass
def badCommand(s:str)->bool:
    return False

def onlineConnectFour():
    ADDRESS = 'woodhouse.ics.uci.edu'
    PORT = 4444
    onlinegame = connectfour.new_game()
    gamesocket = socket.socket()
    try:
        gamesocket.connect((ADDRESS,PORT))
        connectToAI(gamesocket)
        inGame = True
        while inGame:
            user = input('Enter a command: ')
            while (badCommand(user)):
                user = input('Enter a command: ')
            gamesocket.send((user+'\r\n').encode(encoding='utf-8'))
            if (gamesocket.recv(4096).decode(encoding='utf-8').rstrip()=='OKAY'):
                pass
            else:
                print('Invalid Move.')
            print(gamesocket.recv(4096))
            
        
    finally:
        print('Closing connection.')
        gamesocket.close()
    
if __name__ == '__main__':
    onlineConnectFour()
