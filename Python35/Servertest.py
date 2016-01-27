# Echo server program
import socket
from threading import Thread
from collections import namedtuple

class ServerThread(Thread):
    def __init__(self,conn,addr):
        '''Constructor'''
        Thread.__init__(self)
        self.conn = conn
        self.addr = addr
    def run(self):
        while True:
            data = conn.recv(1024)
            print(data)
            if not data: break
            conn.sendall(data)
        conn.close()

class Database():
    def __init__():
        entries = 1w
    def send_to_all(message:str,name:str):
        for x in entries:
            if (x != name)
                entries[x] = message

    def add_entry(name:str):
        entries[name] = ''
    def get_box(name:str)->str:
        temp = entries[name]
        entries[name] = ''
        return temp

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
threads = []
s.bind((HOST, PORT))
s.listen(1)
db = Database()
counter = 0
while True:
    conn, addr = s.accept()
    threads.append(ServerThread(conn,addr))
    threads[-1].start()
    db.add_entry('00'+str(counter))
    print('Connected by', addr)


