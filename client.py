from socket import *
import cv2
import pickle
import struct

#address = input("What is server address? ")
#port = int(input("What is server port? "))

#create a socket
socket = socket(AF_INET, SOCK_STREAM)
#choose server IP and port
address = '192.168.56.1'
port = 9001
#try to connect to server
socket.connect((address, port))

#data will be what we gather from our recv's
data = bytearray()

#keep looping
while True:
    #when we start a frame
    while len(data) < 4:
        #get the header
        packet = socket.recv(4)
        #if no header and data, server is done transmitting
        if not packet:
            break
        #add the packet to our data
        data.extend(packet)
    #read the header
    length = struct.unpack(">I", data[:4])[0]
    #data now excludes header, so we can parse the frame
    data = data[4:]

    #while we don't have the complete frame
    while len(data) < length:
        #keep recv
        packet = socket.recv(4096)
        #print("processing", len(data))
        #and add it to our data
        data.extend(packet)
    #parse our frame from our data
    compressed = data[:length]
    #the rest is for next frame
    data  = data[length:]
    #get our frame from bytestream
    frame = pickle.loads(compressed)
    #display the frame on the UI
    cv2.imshow("Client",frame)
    #every milisecond, check for user key input
    key = cv2.waitKey(1)
    #if the key is Q, then quit the program
    if key == ord('q'):
        socket.close()
        break
    #if the key is a space, then pause the film
    while key in [ord(' ')]:
        key = cv2.waitKey(0)
        if key == ord(' '):
            break
    #quit when 'q' is pressed
    if key == ord('q'):
        socket.close()
        break
