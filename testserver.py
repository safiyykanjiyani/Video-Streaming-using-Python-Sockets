from socket import *
import cv2
import pickle 
import struct


socket = socket(AF_INET, SOCK_STREAM)
address = '192.168.56.1'
port = 9001
socket.bind((address,port))
socket.listen(1)


while True:
    client, addr = socket.accept()
    if client:
        video = cv2.VideoCapture("bird.avi")
        while video.isOpened():
            ret, frame = video.read()
            cv2.imshow("Server", frame)
            compressed = pickle.dumps(frame)
            packet = struct.pack('>I', len(compressed)) + compressed
            #length = struct.unpack('>I', packet[:4])[0]
            #print("frame length:", length)
            #compressed = packet[4:]
            #frame = pickle.loads(compressed)
            client.sendall(packet)
            #cv2.waitKey(1)
            #cv2.imshow("Server", frame)
            if not ret:
                print("last frame")
                break
        video.release()
        cv2.destroyAllWindows()
    socket.close()
