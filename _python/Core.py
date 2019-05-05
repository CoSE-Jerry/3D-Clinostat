import socket
from time import sleep
from picamera import PiCamera

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip_address = "10.0.5.2"
server_address = (ip_address, 23456)
sock.bind(server_address)

sock.listen(1)

while True:
    connection, client_address = sock.accept()

    while True:
        recieved = connection.recv(1024).decode("utf-8")
        print (recieved)

        CMD = data.split('~', 5)

        if(CMD[0]=='A'):
            with PiCamera() as camera:
                camera.resolution = (int(CMD[1]),int(CMD[2]))
                camera._set_rotation(90*int(CMD[3]))
                sleep(2)
                if(int(CMD[4])):
                    camera.capture("out.jpg")
                else:
                    camera.capture("out.png")
            print("imaging done")
            
            if(int(CMD[4])):
                f = open ("out.jpg", "rb")
            else:
                f = open ("out.png", "rb")
            l = f.read(1024)
            while (l):
                connection.send(l)
                l = f.read(1024)
            f.close()
            print("image sent")
            break


        elif(CMD=='P'):
            with PiCamera() as camera:
                camera.resolution = (2464,2464)
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
    



