## Video Streaming Final Project

Dependencies are sockets, pickle, struct, and cv2

cv2 turns video files into individual frame objects and also can display those frame objects

struct is used to pass additional information through a socket (in my case, I needed to inform the client the size of each frame)

pickle can convert objects in Python into bytestreams (in my case I used pickle to transmit the frames as a bytestream through a socket)

sockets are used to transmit bytestreams from a server program to a client program.

### How it works

A server can choose which video to transmit to a client and a client can connect to the server.

After the client connects, the server gets the first frame using cv2 pickle then converts it into a bytestream. It then checks its size and makes a struct with the size and object. The struct is then transmitted to the client.

On the client side, the client reads the size to see how much data it needs to accept, it then converts the bytestream back into a frame and displays it using cv2. After this process, it has the option to pause the stream using **space** or quitting the stream using **Q**. 
