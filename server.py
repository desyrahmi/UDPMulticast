from socket import socket, AF_INET, SOCK_STREAM
import threading

def acceptClient():
    while True:
        cli_sock, cli_add = socket.accept()
        username = cli_sock.recv(1024)
        CONNECTION_LIST.append((username, cli_sock))
        print username, " is now connected."
        threadClient = threading.Thread(target = broadcastUser, args = [username, cli_sock])
        threadClient.start()

def broadcastUser(username, cli_sock):
    while True:
        try:
            data = cli_sock.recv(1024)
            if data:
                print "{0} spoke".format(username)
                b_user(cli_sock, username, data)
        except Exception as x:
            print(x.message)
            break

def b_user(cs_sock, senderName, msg):
    for client in CONNECTION_LIST:
        if client[1] != cs_sock:
            client[1].send(senderName)
            client[1].send(msg)

if __name__ == "__main__":
    CONNECTION_LIST = []
    socket = socket(AF_INET, SOCK_STREAM)

    HOST = '192.168.1.1'
    PORT = 8000