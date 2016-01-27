import socket
from threading import Thread

def read_host() -> str:
    while True:
        host = input('Host: ').strip()

        if len(host) == 0:
            print('Please specify a host (either a name or an IP address)')
        else:
            return host


def read_port() -> int:
    while True:
        try:
            port = int(input('Port: ').strip())

            if port < 0 or port > 65535:
                print('Ports must be an integer between 0 and 65535')
            else:
                return port

        except ValueError:
            print('Ports must be an integer between 0 and 65535')


'''def conduct_echo_conversation(echo_host: str, echo_port: int) -> None:
    echo_socket = socket.socket()

    try:
        print('Connecting to echo server...')
        echo_socket.connect((echo_host, echo_port))

        print('Connected successfully!')
        while True:
            message_to_send = input('Message: ')

            if len(message_to_send) == 0:
                break
            else:
                end + '\r\n').encode(encoding='utf-8')
                echo_socket.send(bytes_to_send)
                response_message_bytes = echo_socket.recv(4096)
                response_message = response_message_bytes.decode(encoding='utf-8').rstrip()

                print('Response: ' + response_message)

    finally:
        print('Closing connection')
        echo_socket.close()

    print('Goodbye!')



if __name__ == '__main__':
    conduct_echo_conversation(read_host(), read_port())'''

class inputThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        cache = ''
    
    def get_cache()->str:
        temp = cache
        cache = ''
        return temp
    
    def run(self):
        while (True):
            getInput = input()
            cache = getInput

def main():
    chat_socket = socket.socket()
    
