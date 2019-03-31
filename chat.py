import socket
import select
import sys
import json

def connectClients(clients):
    clientSocket = []
    for host, port in clients:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host,port))
        clientSocket.append(s)
            
    return client_socket

def sendMessages(seq, msg, clientSocket):
    seq = 0
    for socket in clientSockets:
        jsonMsg = '{"seq": %d, "user": %s, "message": %s}' % (seq, user, msg) # i think this is the JSON way
        socket.sendall(jsonMsg.encode())
        seq += 1
        
def main(user, port, clients):
    HOST = '127.0.0.1' # standard loopback interface address
    
    writeSockets = None
    readSockets = []
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serverSocket:
        serverSocket.bind((HOST, port))
        serverSocket.listen()
        
        while True:
            
            txt = input()
            if txt == 'exit': # made exit work
                exit()
            
            # if writeSockets is None:
            #   writeSockets = connectClients(clients)
            # sendMessages(txt, writeSockets)
            
            rList = [serverSocket]
            rList.extend(readSockets)
            rListOut, _, _ = select.select(rList, [], [])
            
            for s in rListOut:
                if s == serverSocket:
                    conn, addr = s.accept()
                    readSockets.append(conn)
                    
                elif s == sys.stdin:
                    txt = input("here: ")
                    if writeSockets is None:
                        writeSockets = connectClients(clients)
                    sendMessages(txt, writeSockets)
                
                else:
                    # this must be a socket to read from
                    data = s.recv(1024)
                    if not data:
                        print('stopped')
                        break
                    print('recieved ',data.decode())


if __name__ == '__main__':
    if len(sys.argv) < 3:
        sys.exit(-1)
    
    user = sys.argv[1]
    port = int(sys.argv[2])
    
    clients = []
    for arg in sys.argv[3:]:
        chost, cport = arg.split(':')
        cport = int(cport)
        clients.append((chost, cport))
        
    print('user', user)
    print('port', port)
    print('clients', clients)
    main(user, port, clients)
<<<<<<< HEAD
=======
    
    # command is: 
    # >> python chat.py user1 5001 127.0.0.1:5002 127.0.0.1:5003
    # >> python chat.py user2 5002 127.0.0.1:5001 127.0.0.1:5003
    # >> python chat.py user3 5003 127.0.0.1:5001 127.0.0.1:5002
>>>>>>> master
                        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
