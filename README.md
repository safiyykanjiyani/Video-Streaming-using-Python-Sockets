## Video Streaming Final Project

Dependencies are sockets, pickle, struct, and cv2

cv2 turns video files into individual frame objects and also can display those frame objects

struct is used to pass additional information through a socket (in my case, I needed to inform the client the size of each frame)

pickle can convert objects in Python into bytestreams (in my case I used pickle to transmit the frames as a bytestream through a socket)

sockets are used to transmit bytestreams from a server program to a client program.

### How it works
