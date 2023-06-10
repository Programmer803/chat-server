import socket 
import _thread
import time


sock =  socket.socket()
db_con = []
sock.bind(("192.168.1.100",8989))


def send_to_all(msg):
      
      for cli in db_con:
            cli.send(msg)

def MakeConnection():

    sock.listen(1)

    con , cli = sock.accept()

    db_con.append(con)

    print(f"# Connection [{cli[0]}] Port [{cli[1]}]")

    Recv(con)

# Recv data from client
def Recv(con):

    

    # get username
    username = con.recv(1024).decode()

    while 1:
          
          # Log Msg
          msg = str(con.recv(1024).decode())

          if msg:

            print(username+" : "+msg)
            msg = username+" : "+msg

            send_to_all(msg.encode())
      

            
while 1:
        try:
            
        
            _thread.start_new_thread(MakeConnection,())
            time.sleep(2.5)
            _thread.start_new_thread(MakeConnection,())
        except:
             pass
     



    