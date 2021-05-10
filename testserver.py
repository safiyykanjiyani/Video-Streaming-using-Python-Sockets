from socket import *
import cv2
import pickle
import struct

#create a TCP socket
socket = socket(AF_INET, SOCK_STREAM)
#set address and port
address = '192.168.56.1'
port = 9001
#bind to socket and start listening
socket.bind((address,port))
socket.listen(1)
#choose videofile to display!
videofile = "fountain.mp4"

while True:
    #keep looking for clients
    client, addr = socket.accept()
    #if client is present
    if client:
        #open up the video
        video = cv2.VideoCapture(videofile)
        while video.isOpened():
            #grab the frame
            ret, frame = video.read()
            #turn frame into a byte stream
            compressed = pickle.dumps(frame)
            #make a packet whose header has size (in bytes) of the frame
            packet = struct.pack('>I', len(compressed)) + compressed

            '''
            length = struct.unpack('>I', packet[:4])[0]
            print("frame length:", length)
            compressed = packet[4:]
            frame = pickle.loads(compressed)
            '''
            #send the packet to the client
            client.sendall(packet)
            #cv2.waitKey(1)
            #cv2.imshow("Server", frame)
    socket.close()
