import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.1.64"
port = 4455
s.connect((host,port))
print("Connected To The Server")



while True:
    msg = input("Enter Your Msg : ")
    msg = msg.encode()
    s.send(msg)
    print("Sent")
    r_msg = s.recv(1024)
    r_msg = r_msg.decode()
    print("received msg : " + r_msg)