import socket, threading
import time
s = socket.socket()
#binds ip
s.bind(("192.168.1.195", 8888))
#banned
blacklist = []
#connection dict
connections = {}
#dict for code reference
codes = {"msg":"222", "challenge":"798", "error":"545", "throw":"877", "connectr":"133", "done": "099","aord":"344","ping":"111"}
#msgs
msgs=[]
#challenges themselves will make client-side later
challenges = {}
#dict for challenge checker
namechal = {}

def handler(conn, addr):
    mymsgs = []
    #message loop that gets the name of person and says if it is a valid name
    while True:
        try:
            name = conn.recv(1024).decode("utf-8")
            if name not in [x for x in connections]:
                conn.send(bytes("!GOOD", "utf-8"))
                connections[name] = conn
                print("{} connected from {}".format(name, addr))
                break
            else:
                conn.send(bytes("!BAD", "utf-8"))
        except:
            break
    #recieve loop that processes msg
    while True:
        try:
            msg = conn.recv(1024).decode("utf-8")
        except:
            break

        if not msg:
            break
        print(msg)
        if msg[:3] == codes["msg"]:
            for x in connections:
                connections[x].send(bytes(msg[3:],"utf-8"))
        if msg[:3] == codes["challenge"]:
            pass
        if msg[:3] == codes["aord"]:
            pass



    #removes them from connection list
    connections.pop(name)
    #closes connection
    conn.close()
    print("{} has disconnected!".format(addr[0]))


def strt():
    #starts server max 10 connections
    s.listen(10)
    print("Server is running on {}".format(socket.gethostname()))
    #accept connections loop
    while True:
        conn, addr = s.accept()
        #if ip is banned close connection
        if addr in blacklist:
            conn.close()
            continue
        #recieves first message which is a code seperating the connection into its category
        recv = conn.recv(1024).decode("utf-8")
        #not a regular client so no one can join without "code"
        if recv != "197884":
            conn.close()
        #if it is an rpsgame
        elif recv == "163411":
            pass
        #normal client
        else:
            t = threading.Thread(target=handler, args=(conn,addr))
            t.start()

strt()





