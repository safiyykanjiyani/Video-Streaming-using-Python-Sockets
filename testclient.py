from socket import *
import cv2
import pickle
import struct

#address = input("What is server address? ")
#port = int(input("What is server port? "))

socket = socket(AF_INET, SOCK_STREAM)
address = '192.168.56.1'
port = 9001
socket.connect((address, port))

data = bytearray()


while True:
    while len(data) < 4:
        packet = socket.recv(4)
        if not packet:
            break
        data.extend(packet)
    length = struct.unpack(">I", data[:4])[0]
    data = data[4:]

    while len(data) < length:
        packet = socket.recv(4096)
        #print("processing", len(data))
        data.extend(packet)
    compressed = data[:length]
    data  = data[length:]
    frame = pickle.loads(compressed)
    cv2.imshow("Client",frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    while key in [ord(' ')]:
        key = cv2.waitKey(0)
        if key == ord(' '):
            break
# Quit when 'q' is pressed
    if key == ord('q'):
        break
