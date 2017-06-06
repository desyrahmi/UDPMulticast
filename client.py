from socket import socket, AF_INET, SOCK_STREAM
import threading

def send():
    while True:
        msg = raw_input("Enter message: ");
        cli_sock.send(msg)

def receive():
    while True:
        senderName = cli_sock.recv(1024)
        data = cli_sock.recv(1024)

        print ('\n' + str(senderName) + ' > ' + str(data))

if __name__ == "__main__":
    cli_sock = socket(AF_INET, SOCK_STREAM)

    HOST = '192.168.1.1'
    PORT = 8000
    cli_sock.connect((HOST, PORT))
    print ('Connected to remote host')
    username = raw_input('Enter your name to enter the chat > ')
    cli_sock.send(username)

    thread_send = threading.Thread(target = send)
    thread_send.start()

    thread_receive = threading.Thread(target = receive)
    thread_receive.start()