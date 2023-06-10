import socket
import threading
import time



class Connect:

    def __init__(self):

        self.ip = None
        self.port = None
        self.sock = socket.socket()
        self.connect()
        self.m_1 = None
        self.m_2 = None

    def connect(self):

        ip = input("Ip >>> ")
        port = input("Port >>> ")

        self.sock.connect((ip , int(port)))

        username = input("[Usename] >>> ")
        self.sock.send(username.encode())
        self.multi()

    def multi(self):

        while 1:
            self.m_1=threading.Thread(target=self.send)
            self.m_2=threading.Thread(target=self.recv_)

            self.m_1.start()
            time.sleep(2.5)
            self.m_2.start()
            
            
            
            

    def send(self):
        
            
        
            
            msg = input("")

            self.sock.send(str(msg+"\n").encode())

    def recv_(self):
        
            
        try:
            msg_r = self.sock.recv(1024)

            print(msg_r.decode())

        except:
             pass


Connect()



    
