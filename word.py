import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = "192.168.1.64"
port  = 4455
s.bind((server_ip,port))
print("Server Is Running On " + server_ip +" "+ str(port))

s.listen(1)
conn, addr = s.accept()
print("Connected")
print(addr)


while True :
    msg = input("Enter Your Msg : ")
    msg = msg.encode()
    conn.send(msg)
    print("Sent")
    r_msg = conn.recv(1024)
    r_msg = r_msg.decode()
    print(r_msg)
