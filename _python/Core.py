import socket
from time import sleep
from picamera import PiCamera

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip_address = "10.0.5.2"
server_address = (ip_address, 23456)
sock.bind(server_address)

sock.listen(1)

while True:
    print ('waiting for a connection')
    connection, client_address = sock.accept()

    while True:
        CMD = connection.recv(1024).decode("utf-8")

        if(CMD=='A'):
            with PiCamera() as camera:
                camera.resolution = (350,350)
                sleep(2)
                camera.capture("out.jpg")
            print("imaging done")
            f = open ("out.jpg", "rb")
            l = f.read(1024)
            while (l):
                connection.send(l)
                l = f.read(1024)
            f.close()
            print("image sent")
            break
    connection.close()
    



